# Get number from user
number = int(input())

if number == 1:
    print(number)
    exit()

# Create matrix (list) of size num x num and populate with 0
matrix = [[0] * number for i in range(number)]

# Create sequence (list) of numbers from 1 up to num * num
square_seq = list(range(1, number * number + 1))

# Create lists to store decreasing matrix sizes
# h_seq starts with num
# v_seq starts with num - 1
h_seq = list(reversed(range(1, number + 1)))
v_seq = list(reversed(range(1, number)))

# Define starting position for row and column
row = 0
col = -1

# Create 3 logical controllers for movement direction:
# left_to_right, top_to_bottom, vertical_fill or horizontal_fill
l_to_r = True
t_to_b = False
h_fill = True

# Create 2 variables to control if the end of current filling process is reached
h_seq_counter = 0
v_seq_counter = 0
h_counter = h_seq[h_seq_counter]
v_counter = v_seq[v_seq_counter]

# Iterate over the square sequence:
for num in square_seq:
    # print(matrix)
    if v_counter == 0:
        h_fill = not h_fill
        l_to_r = not l_to_r
        v_seq_counter += 1
        try:
            v_counter = v_seq[v_seq_counter]
        except IndexError:
            pass

    if h_counter == 0:
        h_fill = not h_fill
        t_to_b = not t_to_b
        h_seq_counter += 1
        try:
            h_counter = h_seq[h_seq_counter]
        except IndexError:
            pass

    # Horizontal fill left to right
    if h_fill and l_to_r:
        col += 1
        matrix[row][col] = num
        h_counter -= 1

    # Horizontal fill right to left
    elif h_fill and not l_to_r:
        col -= 1
        matrix[row][col] = num
        h_counter -= 1

    # Vertical fill top to bottom:
    elif not h_fill and t_to_b:
        row += 1
        matrix[row][col] = num
        v_counter -= 1

    # Vertical fill bottom to top
    elif not h_fill and not t_to_b:
        row -= 1
        matrix[row][col] = num
        v_counter -= 1

for line in matrix:
    print(*line)
