def find_set(x):
    return x if p[x] == x else find_set(p[x])


def union(x,y):
    p[find_set(y)] = find_set(x)


def kruskal():
    edges = []
    for edge in mst:
        if find_set(edge[0]) != find_set(edge[1]):
            edges.append(edge)
            union(edge[0], edge[1])
    return edges


T = int(input())
for tc in range(1, T+1):
    V,E = map(int, input().split())
    mst = [list(map(int, input().split())) for _ in range(E)]
    mst.sort(key=lambda x: x[2])
    p = [i for i in range(V+1)]
    dist = 0

    edges = kruskal()
    for i in edges:
        dist += i[2]
    print('#{} {}'.format(tc, dist))