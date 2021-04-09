T = int(input())
dx = [0, 1]
dy = [1, 0]

def DFS(x,y,now):
    global move
    for i in range(2):
        a,b = x+dx[i],y+dy[i]
        if 0 <= a < N and 0 <= b < N:
            now += base[a][b]
            DFS(a,b,now)
            now -= base[a][b]
            if move != base[0][0] and now > move:
                break
            if a == b == N-1:
                if move == base[0][0] or now < move:
                    move = now

for tc in range(1, T+1):
    N = int(input())
    base = [list(map(int, input().split())) for _ in range(N)]
    move = base[0][0]
    DFS(0,0,move)
    print('#{} {}'.format(tc, move+base[N-1][N-1]))