import torch

def train(model, X_train, label_embedding, y_train,
          total_epoch=250, batch_size=250, learning_rate=0.001,
          save_path='./model.pt', state=None):

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)
    label_embedding = label_embedding.to(device)
    criterion = nn.BCEWithLogitsLoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    train_data = DataLoader(dataset(X_train, y_train), batch_size=batch_size)

    best_loss = float('inf')
    num_increasing_epochs = 0

    for epoch in range(1, total_epoch + 1):
        running_loss = 0
        y_pred = []
        epoch_time = 0
        model.train()

        for index, (X, y) in enumerate(train_data):
            optimizer.zero_grad()
            out = model(X.to(device), label_embedding)
            loss = criterion(out, y.to(device).float())
            loss.backward()
            nn.utils.clip_grad_norm_(model.parameters(), max_norm=10)
            optimizer.step()
            y_pred.append(torch.sigmoid(out.detach()).round().cpu())
            running_loss += loss.item()

        y_pred = torch.vstack(y_pred)
        f1score = f1_score(y_train, y_pred, average='micro')
        recallscore = recall_score(y_train, y_pred, average='micro')
        hammingloss = hamming_loss(y_train, y_pred)
        print(f'epoch:{epoch} loss:{running_loss:.5f} hamming_loss:{hammingloss:.5f} micro_f1score:{f1score:.5f} micro_recallscore:{recallscore:.5f}')