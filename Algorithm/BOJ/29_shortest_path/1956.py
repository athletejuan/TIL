V,E = map(int, input().split())
adjgo = [[10000*V]*(V+1) for _ in range(V+1)]
adjback = [[10000*V]*(V+1) for _ in range(V+1)]
for i in range(E):
    a,b,c = map(int, input().split())
    adjgo[a][b] = adjback[b][a] = c
shortest = 10000*V

def Dijkstra(s, D, adj):
    visited = [0] * (V+1)
    D[s] = 0

    for i in range(V-1):
        dist = 10000*V
        for j in range(1, V+1):
            if not visited[j] and dist > D[j]:
                dist = D[j]
                c = j
        visited[c] = 1

        for k in range(1, V+1):
            if not visited[k] and D[k] > dist + adj[c][k]:
                D[k] = dist + adj[c][k]
    return D

for i in range(1, V+1):
    short_go = Dijkstra(i, adjgo[i], adjgo)
    short_back = Dijkstra(i, adjback[i], adjback)
    for j in range(1, V+1):
        if i != j:
            short = short_go[j] + short_back[j]
            if short < shortest:
                shortest = short
print(shortest if shortest < 10000*V else -1)