line = 'a4b12c1d8k11a4'

letters = []
numbers = []
combined = []
pos = 0

while pos < len(line):

    slider = pos + 1

    while slider < len(line) and line[slider].isdigit():
        slider += 1

    letters.append(line[pos])
    numbers.append(line[pos + 1: slider])

    combined.append({line[pos]: line[pos + 1: slider]})

    pos = slider

print(letters)  # ==> ['a', 'b', 'c', 'd', 'k', 'a']
print(numbers)  # ==> ['4', '12', '1', '8', '11', '4']

print(combined)  # ==> [{'a': '4'}, {'b': '12'}, {'c': '1'}, {'d': '8'}, {'k': '11'}, {'a': '4'}]
