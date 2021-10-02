T = int(input())
dx = [0, 1]
dy = [1, 0]

def DFS(x,y,now):
    global move
    if x == y == N-1:
        if move == base[0][0] or now < move:
            move = now
            return
    if move != base[0][0] and now > move:
        return
    for i in range(2):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            DFS(nx, ny, now + base[nx][ny])

for tc in range(1, T+1):
    N = int(input())
    base = [list(map(int, input().split())) for _ in range(N)]
    move = base[0][0]
    DFS(0,0,move)
    print('#{} {}'.format(tc, move))