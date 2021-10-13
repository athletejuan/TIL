def BFS():
    q = [[0, 0]]
    while q:
        r,c = q.pop(0)
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                diff = 0
                if region[nr][nc] > region[r][c]:
                    diff = region[nr][nc]-region[r][c]
                if cost[nr][nc] > cost[r][c] + diff + 1:
                    cost[nr][nc] = cost[r][c] + diff + 1
                    q.append([nr, nc])
    return cost[N-1][N-1]


T = int(input())
dr, dc = [1, 0, -1, 0], [0, 1, 0, -1]

for tc in range(1, T+1):
    N = int(input())
    region = [list(map(int, input().split())) for _ in range(N)]
    cost = [[N * 1000] * N for _ in range(N)]
    cost[0][0] = 0
    print('#{} {}'.format(tc, BFS()))