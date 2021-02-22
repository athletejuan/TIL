R,C = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

pasture = [list(input()) for _ in range(R)]
clump = []
num = 0

def DFS():
    while clump:
        now = clump.pop()
        x, y = now[0], now[1]
        pasture[x][y] = '.'
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a < R and 0 <= b < C and pasture[a][b] == '#':
                clump.append([a,b])

for i in range(R):
    for j in range(C):
        if pasture[i][j] == '#':
            clump.append([i,j])
            DFS()
            num += 1

print(num)