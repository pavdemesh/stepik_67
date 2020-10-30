# Create empty list
matrix = list()

# Get input from user
while True:
    line = input()
    # Check if input == "end", break
    if line == "end":
        break
    # Else convert input to a list of ints and append to the matrix list
    else:
        matrix.append([int(i) for i in line.split()])

# Create variables to store the count of row and cols in the matrix
row_count = len(matrix)
col_count = len(matrix[0])

# Generate matrix of same size populated with 0
res = [[0] * col_count for i in range(row_count)]

for row in range(row_count):
    for col in range(col_count):
        n_1 = matrix[row - 1][col]
        n_2 = matrix[row - row_count + 1][col]
        n_3 = matrix[row][col - 1]
        n_4 = matrix[row][col - col_count + 1]
        res[row][col] = n_1 + n_2 + n_3 + n_4

for item in res:
    print(*item)
