C,R = map(int, input().split())
base = [list(map(int, input().split())) for _ in range(C)]
remain = [0] * 50
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0

def BFS():
    global cnt
    cnt += 1
    now = [[0, 0]]
    visited = [[0] * R for _ in range(C)]
    air, cheeze = [[0, 0]], []
    while air:
        air = []
        while now:
            x,y = now.pop()
            visited[x][y] = 1
            for i in range(4):
                a,b = x+dx[i],y+dy[i]
                if 0 <= a < C and 0 <= b < R and not visited[a][b]:
                    if not base[a][b]:
                        air.append([a,b])
                        visited[a][b] = 1
                    else:
                        cheeze.append([a,b])
                        visited[a][b] = 1
        now = air

    remain[cnt] = len(cheeze)
    for i in cheeze:
        base[i[0]][i[1]] = 0
    if not cheeze:
        print(cnt-1)
        print(remain[cnt-1])
        return
    BFS()
BFS()