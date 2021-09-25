T = int(input())

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def DFS(r, c, k, cnt, field, visited):
    global long
    if long < cnt:
        long = cnt
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and field[nr][nc] - field[r][c] < k:
            gap = field[nr][nc] - field[r][c] + 1
            if gap < 0: gap = 0
            flag = k - gap
            if gap > 0: flag = 0
            field[nr][nc] -= gap
            visited[nr][nc] = 1
            DFS(nr, nc, flag, cnt+1, field, visited)
            field[nr][nc] += gap
            visited[nr][nc] = 0


for tc in range(1, T+1):
    N,K = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    altitude = long = 0
    for i in range(N):
        for j in range(N):
            if field[i][j] < altitude:
                continue
            if field[i][j] > altitude:
                altitude = field[i][j]
                tiptop = []
            tiptop.append([i, j])

    for r,c in tiptop:
        visited[r][c] = 1
        DFS(r, c, K, 1, field, visited)
        visited[r][c] = 0
    print('#{} {}'.format(tc, long))