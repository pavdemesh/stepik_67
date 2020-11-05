d = int(input())
vocab = list()

for i in range(d):
    entry = input().lower()
    vocab.append(entry)

# print(vocab)

k = int(input())
txt = []

for j in range(k):
    line = input().lower().split()
    txt += line

# print(txt)

errors = []
for word in txt:
    if word not in vocab:
        errors.append(word)

for res in set(errors):
    print(res)
