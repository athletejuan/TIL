T = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS(x,y):
    arr = [[x,y]]
    cnt = 1
    start = rooms[x][y]
    while arr:
        for i in range(len(arr)):
            x,y = arr.pop(0)
            now = rooms[x][y]
            for i in range(4):
                a,b = x + dx[i], y + dy[i]
                if 0 <= a < N and 0 <= b < N:
                    if rooms[a][b] == now+1:
                        cnt += 1
                        arr.append([a,b])
    move[start] = cnt

for tc in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    move = {}
    for i in range(N):
        for j in range(N):
            BFS(i,j)
    max_move = sorted(move, key=lambda x: (-move[x], x))[0]
    print('#{} {} {}'.format(tc, max_move, move[max_move]))