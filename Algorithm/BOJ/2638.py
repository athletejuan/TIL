N,M = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

cnt = 0
while True:
    stack = [[0,0]]
    air = [[0]*M for _ in range(N)]
    while stack:
        r,c = stack.pop()
        air[r][c] = 1
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and not field[nr][nc] and not air[nr][nc]:
                stack.append([nr, nc])
    cheese = []
    flag = True
    for i in range(N):
        for j in range(M):
            if field[i][j]:
                flag = False
                cheese.append([i,j])
    if flag:
        break
    for r,c in cheese:
        exo = 0
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if air[nr][nc]:
                exo += 1
        if exo > 1:
            field[r][c] = 0
    cnt += 1

print(cnt)