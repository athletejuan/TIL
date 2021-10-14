def find_set(x):
    return x if x == p[x] else find_set(p[x])


def union(x,y):
    p[find_set(y)] = find_set(x)


def kruskal():
    global weight
    for edge in edges:
        if find_set(edge[0]) != find_set(edge[1]):
            weight += edge[2]
            union(edge[0], edge[1])


V = int(input())
E = int(input())
edges = [list(map(int, input().split())) for _ in range(E)]
edges.sort(key=lambda x: x[2])
p = [i for i in range(V+1)]
weight = 0

kruskal()
print(weight)