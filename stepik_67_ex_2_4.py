seq = input()

counter = 0

for i in range(len(seq)):

    if i == 0:
        print(seq[i], end='')
        counter += 1

    elif seq[i] == seq[i - 1]:
        counter += 1

    else:
        print(counter, seq[i], sep='', end='')
        counter = 1
print(counter)
