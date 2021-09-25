from collections import deque

T = int(input())

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def BFS(Q):
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if field[nr][nc] == 'L' and dist[r][c]+1 < dist[nr][nc]:
                    Q.append([nr, nc])
                    dist[nr][nc] = dist[r][c] + 1


for tc in range(1, T+1):
    N,M = map(int, input().split())
    field = [input() for _ in range(N)]
    dist = [[2000] * M for _ in range(N)]
    Q, total = deque(), 0

    for i in range(N):
        for j in range(M):
            if field[i][j] == 'W':
                Q.append([i,j])
                dist[i][j] = 0
    BFS(Q)

    for k in range(N):
        for l in range(M):
            total += dist[k][l]
    print('#{} {}'.format(tc, total))