def DFS(r,c):
    space = 1
    stack = [[r,c]]
    while stack:
        r,c = stack.pop()
        paper[r][c] = 1
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < M and 0 <= nc < N and not paper[nr][nc]:
                stack.append([nr, nc])
                paper[nr][nc] = 1
                space += 1
    return space


M,N,K = map(int, input().split())
dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
paper = [[0] * N for _ in range(M)]
cnt, area = 0, []
for i in range(K):
    x,y,z,w = map(int, input().split())
    for r in range(y, w):
        for c in range(x, z):
            paper[r][c] = 1

for j in range(M):
    for k in range(N):
        if not paper[j][k]:
            cnt += 1
            area.append(DFS(j,k))
print(cnt)
print(*sorted(area))
