N,M = map(int, input().split())

maze = [list(map(int, list(input()))) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
visited[0][0] = 1
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
q = [(0,0)]

while q:
    y,x = q.pop(0)
    if x == M-1 and y == N-1:
        print(visited[y][x])
        break
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if not visited[ny][nx] and maze[ny][nx]:
                q.append((ny, nx))
                visited[ny][nx] = visited[y][x] + 1