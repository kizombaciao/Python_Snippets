import pickle

data = {
    'a': [1, 2, 3],
    'b': 'abc',
    (1, 2): [1, 2]
}

with open("test.pkl", "wb") as f:
    pickle.dump(data, f)

del data

with open("test.pkl", "rb") as f:
    data = pickle.load(f)

print(data)