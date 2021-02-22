dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DFS():
    while infested:
        now = infested.pop()
        x, y = now[0], now[1]
        Mirk[x][y] = 'S'
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a < H and 0 <= b < W and Mirk[a][b] == 'T':
                infested.append([a,b])

while True:
    W,H = map(int, input().split())
    if not int(W):
        break

    Mirk = [list(input()) for _ in range(H)]
    infested = []

    for i in range(H):
        for j in range(W):
            if Mirk[i][j] == 'S':
                infested.append([i,j])
                DFS()

    for k in range(H):
        print(''.join(Mirk[k]))
