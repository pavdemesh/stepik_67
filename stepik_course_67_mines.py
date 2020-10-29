rows_total, cols_total, mines_total = (int(i) for i in input().split())  # чтение размеров поля и числа мин

field = [[0 for j in range(cols_total)] for i in range(rows_total)]  # заполнение поля нулями

for i in range(mines_total):
    row, col = (int(i) - 1 for i in input().split())
    field[row][col] = -1  # расставляем мины

for i in range(rows_total):
    for j in range(cols_total):
        if field[i][j] == 0:  # в этой клетке мины нет, поэтому считаем число мин вокруг
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ai = i + di
                    aj = j + dj
                    # (ai, aj)
                    if 0 <= ai < rows_total and 0 <= aj < cols_total and field[ai][aj] == -1:
                        field[i][j] += 1
# вывод результата
for i in range(rows_total):
    for j in range(cols_total):
        if field[i][j] == -1:
            print('*', end='')
        elif field[i][j] == 0:
            print('.', end='')
        else:
            print(field[i][j], end='')
    print()