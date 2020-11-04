n = int(input())

x, y, b, a, t = 0, 0, 0, 1, [[0]*n for i in range(n)]

for i in range(n*n):

    t[x][y] = i+1

    if t[(x+b) % n][(y+a) % n] != 0:
        b, a = a, -b

    x, y = x + b, y + a

[print(*i, sep='\t') for i in t]
