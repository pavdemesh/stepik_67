def rec(matrix, i_, j_, n, start):
    if n == 0:
        return
    if n == 1:
        matrix[i_][j_] = start
        return
    for j in range(j_, j_ + n):
        matrix[i_][j], start = start, start + 1

    for i in range(i_ + 1, i_ + n):
        matrix[i][j_ + n - 1], start = start, start + 1

    for j in range(j_ + n - 2, j_ - 1, -1):
        matrix[i_ + n - 1][j], start = start, start + 1

    for i in range(i_ + n - 2, i_, -1):
        matrix[i][j_], start = start, start + 1

    rec(matrix, i_ + 1, j_ + 1, n - 2, start)


num = int(input())

res = [[0] * num for i in range(num)]

rec(res, 0, 0, num, 1)

[print(*res[i], sep='\t') for i in range(num)]
