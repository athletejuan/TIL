def prim(s):
    key = [float('INF')] * N
    key[s] = 0

    for i in range(N-1):
        tax = float('INF')
        for j in range(N):
            if not visited[j] and key[j] < tax:
                tax = key[j]
                c = j
        visited[c] = 1

        for k in range(N):
            if not visited[k] and adj[c][k]:
                key[k] = min(key[k], adj[c][k])
    return sum(key)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))
    E = float(input())
    adj = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            adj[i][j] = adj[j][i] = (xs[i]-xs[j])**2+(ys[i]-ys[j])**2
    visited = [0] * N
    print('#{} {}'.format(tc, round(prim(0)*E)))