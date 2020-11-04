with open('dataset_3363_2.txt', 'r') as fh:
    line = fh.readline().strip()

list_letters = []
list_numbers = []

tmp = ''

for char in line:
    if char in '0123456789':
        tmp += char
    elif len(list_letters) == 0:
        list_letters.append(char)
    else:
        list_letters.append(char)
        list_numbers.append(int(tmp))
        tmp = ''

list_numbers.append(int(tmp))

output = "".join([list_letters[i] * list_numbers[i] for i in range(len(list_numbers))])

with open('output.txt', 'w') as out:
    out.write(output)
