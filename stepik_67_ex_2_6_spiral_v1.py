number = int(input())
matrix = [[0] * number for h in range(number)]

row, col = 0, 0

for num in range(1, number * number + 1):

    matrix[row][col] = num

    if num == number * number:
        break
    if row <= col + 1 and row + col < number - 1:
        col += 1
    elif row < col and row+col >= number-1:
        row += 1
    elif row >= col and row+col > number-1:
        col -= 1
    elif row > col + 1 and row + col <= number - 1:
        row -= 1

for row in range(number):
    print(*matrix[row])
