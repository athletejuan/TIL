def Dijkstra(s, D):
    visited[s] = 1

    for i in range(N):
        dist = N*10
        for j in range(N+1):
            if not visited[j] and D[j] < dist:
                dist = D[j]
                c = j
        visited[c] = 1

        for k in range(N+1):
            if not visited[k]:
                D[k] = min(D[k], D[c] + cities[c][k])


T = int(input())

for tc in range(1, T+1):
    N,E = map(int, input().split())
    cities = [[N*10] * (N+1) for _ in range(N+1)]
    for _ in range(E):
        s,e,w = map(int, input().split())
        if cities[s][e] > w:
            cities[s][e] = w
    visited = [0] * (N+1)

    Dijkstra(0, cities[0])
    print('#{} {}'.format(tc, cities[0][N]))