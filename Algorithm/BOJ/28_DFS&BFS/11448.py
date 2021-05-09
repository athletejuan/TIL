T = int(input())
dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, -1, 1, 1, -1]

def DFS():
    global w_cnt
    while white:
        now = white.pop()
        x,y = now[0], now[1]
        board[x][y] = 'w'
        for i in range(8):
            a,b = x + dx[i], y + dy[i]
            if 0 <= a < N and 0 <= b < N and board[a][b] == '-' and [a,b] not in white:
                w_cnt += 1
                white.append([a,b])

for tc in range(T):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    white = []
    w_cnt = 0

    for i in range(N):
        for j in range(N):
            if board[i][j] == 'w':
                white.append([i, j])
                DFS()
    print(w_cnt)