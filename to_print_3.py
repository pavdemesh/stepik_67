n = int(input())

x, y, dx, dy, m = 0, 0, 0, 1, [[0]*n for i in range(n)]

for i in range(n*n):
    m[x][y] = i+1
    if x + dx >= n or x+dx < 0 or y+dy >= n or y+dy < 0 or m[x+dx][y+dy]:
        dx, dy = dy, -dx
    x, y = x + dx, y + dy

[print(*i, sep='\t') for i in m]
