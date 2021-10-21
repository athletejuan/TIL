N,M = map(int, input().split())
cubes = [list(map(int, input().split())) for _ in range(N)]
surface = N*M*2

dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

for r in range(N):
    for c in range(M):
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if cubes[r][c] > cubes[nr][nc]:
                    surface += cubes[r][c] - cubes[nr][nc]
            else:
                surface += cubes[r][c]

print(surface)