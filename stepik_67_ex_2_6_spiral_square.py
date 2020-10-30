# Get number from user
num = input()
if len(num) < 1:
    num = 5
else:
    num = int(num)

# Create matrix (list) of size num x num and populate with 0
matrix = [[0] * num for i in range(num)]

# Declare variables to store the count of rows and cols
rows_count = num
cols_count = num
