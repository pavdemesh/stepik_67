x, i, j = 1, 0, 0
n = int(input())

a = [[0]*n for r in range(n)]

a[n//2][n//2] = n**2

for s in range(n//2):
    for rotate in range(4):
        for j in range(n-1-s*2):
            a[i+s][j+s] = x
            x = x+1
        a = [[a[i][j] for i in range(n)] for j in range(n-1, -1, -1)]

for i in a:
    print(*i, sep='\t')
