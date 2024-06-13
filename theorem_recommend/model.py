
class TheoremRecommend(nn.Module):
  def __init__(self, input_size, hidden_size, adjacency, embeddings, heads=4, slope=0.01, dropout=0.5):
    super(TheoremRecommend, self).__init__()
    self.embedding = nn.Embedding.from_pretrained(embeddings)
    self.biLSTM = nn.LSTM(input_size,hidden_size,batch_first=True,bidirectional=True)
    self.adjacency = nn.Parameter(adjacency)
    self.dropout = nn.Dropout(dropout)
    self.edge_weights = nn.Linear(hidden_size*2*2, 1, bias=False)
    self.activation = nn.LeakyReLU(slope)
    self.softmax = nn.Softmax(dim=1)
    self.tanh = nn.Tanh()
    self.heads = heads
    self.transform_dim1 = nn.Linear(input_size, hidden_size*2, bias=False)
    self.transform_dim2 = nn.Linear(hidden_size*2, hidden_size*2, bias=False)
    self.transform_dimensions = [self.transform_dim1, self.transform_dim2]

  def forward(self, token, label_embedding):
      #BILSTM part
      features = self.embedding(token)
      out, (h, _) = self.biLSTM(features)
      embedding = torch.cat([h[-2, :, :], h[-1, :, :]], dim=1)
      embedding = self.dropout(embedding)

      #GAT PART
      for td in self.transform_dimensions: #Two Multiheaded GAT layers
        outputs = []
        for head in range(self.heads):
          label_embed = td(label_embedding)
          n, embed_size = label_embed.shape

          label_embed_combinations = label_embed.unsqueeze(1).expand(-1, n, -1)
          label_embed_combinations = torch.cat([label_embed_combinations, label_embed.unsqueeze(0).expand(n, -1, -1)], dim=2)
          e = self.activation(self.edge_weights(label_embed_combinations).squeeze(2))

          attention_coefficients = self.tanh(torch.mul(e,self.adjacency))

          new_h = torch.matmul(attention_coefficients.to(label_embed.dtype), label_embed)
          outputs.append(new_h)
        outputs = self.activation(torch.mean(torch.stack(outputs, dim=0),dim=0))

        label_embedding = outputs
      attention_features = self.dropout(label_embedding)
      attention_features = attention_features.transpose(0, 1)
      predicted_labels = torch.matmul(embedding, attention_features)
      return predicted_labels