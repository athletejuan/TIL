T = int(input())

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
tunnel = [[1, 1, 1, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1], [1, 0, 0, 1]]


def BFS():
    global cnt, L
    q, temp = [[R, C]], []
    while q and L > 1:
        r, c = q.pop()
        now = under[r][c]
        for idx, dir in enumerate(now):
            if dir:
                nr, nc = r + dr[idx], c + dc[idx]
                if 0 <= nr < N and 0 <= nc < M and under[nr][nc] and under[nr][nc][(idx + 2) % 4] and not visited[nr][nc]:
                    cnt += 1
                    temp.append([nr, nc])
                    visited[nr][nc] = 1
        if not q:
            q, temp, L = temp, [], L - 1
    return cnt


for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    under = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    visited[R][C] = 1
    cnt = 1

    for i in range(N):
        for j in range(M):
            if under[i][j]:
                under[i][j] = tunnel[under[i][j] - 1]
    print('#{} {}'.format(tc, BFS()))


# live
# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]
# connect = [2, 3, 0, 1]  # 연결된 정보
# pipe = [
#     [0, 0, 0, 0],
#     [1, 1, 1, 1],  # 상하좌우
#     [0, 1, 0, 1],  # 상하
#     [1, 0, 1, 0],  # 좌우
#     [1, 0, 0, 1],  # 상우
#     [1, 1, 0, 0],  # 하우
#     [0, 1, 1, 0],  # 하좌
#     [0, 0, 1, 1],  # 상좌
# ]
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N, M, R, C, L = map(int, input().split())
#     # 지도 정보
#     tunnel = [list(map(int, input().split())) for _ in range(N)]
#     visited = [[0] * M for _ in range(N)]
#
#     Q = [(R, C)]
#     visited[R][C] = 1
#
#     ans = 0
#
#     while Q:
#         r, c = Q.pop(0)
#         ans += 1
#         if visited[r][c] >= L: continue
#
#         # 사방향 탐색
#         for d in range(4):
#             curr_p = tunnel[r][c]
#             # 현재 바라보는 방향으로 길이 x
#             if pipe[curr_p][d] == 0: continue
#
#             nr = r + dr[d]
#             nc = c + dc[d]
#
#             # 다음좌표가 맵을 벗어났다면
#             if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
#
#             # nd = (d + 2) % 4
#             nd = connect[d]
#             np = tunnel[nr][nc]
#
#             # 방문을 했거나, 다음 좌표의 파이프가 현재좌표와 연결되지 않는다면
#             if visited[nr][nc] or pipe[np][nd] == 0: continue
#
#             visited[nr][nc] = visited[r][c] + 1
#             Q.append((nr,nc))
#
#     print("#{} {}".format(tc, ans))
