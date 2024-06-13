
train_df = pd.read_csv('pred_seqs_multi_label.csv')
arr=[]
for i in range(train_df.shape[0]):
  if (train_df.iloc[i,2:]==0).all():
    arr.append(1)
  else:
    arr.append(0)
train_df['clean'] = pd.Series(np.asarray(arr))
labels = train_df.columns[2:]
print("Labels:",labels)

train_df = preprocess_text(train_df) # 预处理


X = train_df
y = train_df.iloc[:,2:].values
X_train_with_id, X_test_with_id, y_train, y_test = train_test_split(X, y, test_size=601, shuffle=False)
X_train = X_train_with_id["problem_text"].values
X_test = X_test_with_id["problem_text"].values
test_id_list = X_test_with_id["id"].values

