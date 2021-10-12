import sys
input = sys.stdin.readline


def Dijkstra(s, D):
    visited[s] = 1

    for _ in range(N-1):
        fare = 100000*N
        for i in range(1, N+1):
            if not visited[i] and fare > D[i]:
                fare = D[i]
                w = i
        visited[w] = 1

        for j in range(1, N+1):
            if w != j and not visited[j]:
                D[j] = min(D[j], D[w] + cities[w][j])


N = int(input())
M = int(input())
cities = [[100000*N]*(N+1) for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    a,b,f = map(int, input().split())
    if cities[a][b] > f:
        cities[a][b] = f
s,g = map(int, input().split())
Dijkstra(s, cities[s])
print(cities[s][g])