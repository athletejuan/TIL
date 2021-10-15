def Dijkstra(s,adj):
    visited = [0] * (N+1)
    visited[s] = 1

    for i in range(N-1):
        time = N*100
        for j in range(1, N+1):
            if not visited[j] and time > adj[s][j]:
                time = adj[s][j]
                c = j
        visited[c] = 1

        for k in range(1, N+1):
            if not visited[k]:
                adj[s][k] = min(adj[s][k], time + adj[c][k])
    return adj[s]


T = int(input())
for tc in range(1, T+1):
    N,M,X = map(int, input().split())
    adjgo = [[N*100]*(N+1) for _ in range(N+1)]
    adjcome = [[N*100]*(N+1) for _ in range(N+1)]
    for i in range(M):
        x,y,c = map(int, input().split())
        adjgo[x][y] = c
        adjcome[y][x] = c

    go = Dijkstra(X, adjgo)
    back = Dijkstra(X, adjcome)
    longest = 0
    for j in range(1, N+1):
        if j != X:
            goback = go[j] + back[j]
            if longest < goback:
                longest = goback
    print('#{} {}'.format(tc, longest))


# live
# import sys
# sys.stdin = open('input.txt')
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M, X = map(int, input().split())  # N:사람수, M:간선수, X:생일파뤼집
#
#     adj1 = [[987654321] * (N+1) for _ in range(N+1)]  # 원래입력 (진출)
#     adj2 = [[987654321] * (N+1) for _ in range(N+1)]  # 뒤집은입력 (진입)
#
#     for _ in range(M):
#         x, y, c = map(int, input().split())  # c가중치
#         adj1[x][y] = c
#         adj2[y][x] = c
#
#     dist1 = [987654321] * (N+1)
#     dist2 = [987654321] * (N+1)
#
#     # 다익스트라 호출
#
#     max_value = 0
#
#     for i in range(1, N+1):
#         if dist1[i] + dist2[i] > max_value:
#             max_value = dist1[i] + dist2[i]
#
#     print("#{} {}".format(tc, max_value))