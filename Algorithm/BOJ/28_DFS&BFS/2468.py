N = int(input())
region = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

bottom, top, safe = 100, 0, 1
for i in range(N):
    for j in range(N):
        if region[i][j] < bottom:
            bottom = region[i][j]
        if region[i][j] > top:
            top = region[i][j]

def BFS():
    visited = [[0] * N for _ in range(N)]
    queue, land = [], 0
    for i in range(N):
        for j in range(N):
            if region[i][j] > h and not visited[i][j]:
                land += 1
                visited[i][j] = 1
                queue.append([i, j])
                while queue:
                    x, y = queue.pop(0)
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < N and 0 <= ny < N and region[nx][ny] > h and not visited[nx][ny]:
                            queue.append([nx, ny])
                            visited[nx][ny] = 1
    return land

for h in range(bottom, top):
    temp = BFS()
    if temp > safe:
        safe = temp
print(safe)