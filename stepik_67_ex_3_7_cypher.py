source_line = input()
target_line = input()

line_to_encode = input()
line_to_decode = input()

dict_encode = {}
dict_decode = {}

for i in range(len(source_line)):
    dict_encode[source_line[i]] = target_line[i]
    dict_decode[target_line[i]] = source_line[i]

encoded_line = ''
decoded_line = ''

for char in line_to_encode:
    encoded_line += dict_encode[char]

for char in line_to_decode:
    decoded_line += dict_decode[char]

print(encoded_line)
print(decoded_line)
