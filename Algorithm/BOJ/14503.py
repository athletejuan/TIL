N,M = map(int, input().split())
r,c,d = map(int, input().split())

field = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

cnt = 1
stack = [[r,c]]
while stack:
    r,c = stack.pop()
    visited[r][c] = 1
    for i in range(4):
        nr, nc = r + dr[d], c + dc[d]
        d = (d-1)%4
        if 0 <= nr < N and 0 <= nc < M and not field[nr][nc] and not visited[nr][nc]:
            stack.append([nr, nc])
            cnt += 1
            break
    else:
        nr, nc = r + dr[(d-1)%4], c + dc[(d-1)%4]
        if not field[nr][nc]:
            stack.append([nr, nc])

print(cnt)