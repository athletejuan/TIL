N = int(input())
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def BFS(x,y):
    color = base[x][y]
    queue = [[x,y]]
    visited[x][y] = 1
    while queue:
        x,y = queue[0][0],queue[0][1]
        del queue[0]
        if color == 'G':
            base[x][y] = 'R'
        for i in range(4):
            a,b = x+dx[i], y+dy[i]
            if 0 <= a < N and 0 <= b < N and base[a][b] == color and not visited[a][b]:
                queue.append([a,b])
                visited[a][b] = 1

base = [list(input()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

cnt, rg = 0, 0

for i in range(N):
    for j in range(N):
        if not visited[i][j] and base[i][j]:
            cnt += 1
            BFS(i, j)

visited = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j] and base[i][j]:
            rg += 1
            BFS(i, j)
print(cnt, rg)