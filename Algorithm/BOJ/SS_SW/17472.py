N,M = map(int, input().split())
earth = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [1, 0], [0, 1]
dist, num = 0, 1
mst = []

def numbering(x,y,z):
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    island = [[x,y]]
    while island:
        x,y = island.pop()
        earth[x][y] = z
        for k in range(4):
            a, b = x+dx[k], y+dy[k]
            if 0 <= a < N and 0 <= b < M and earth[a][b] == 1 and [a,b] not in island:
                island.append([a,b])

def bridge(x,y,z,l,n):
    a, b = x+dx[z], y+dy[z]
    if 0 <= a < N and 0 <= b < M:
        if earth[a][b]:
            if l == 1:
                return
            if n != earth[a][b] and [n,earth[a][b],l] not in mst:
                mst.append([n,earth[a][b],l])
            return
        elif not earth[a][b]:
            bridge(a,b,z,l+1,n)

for i in range(N):
    for j in range(M):
        if earth[i][j] == 1:
            num += 1
            numbering(i,j,num)

for i in range(N):
    for j in range(M):
        if earth[i][j]:
            for k in range(2):
                a, b = i+dx[k], j+dy[k]
                if 0 <= a < N and 0 <= b < M:
                    if not earth[a][b]:
                        bridge(a,b,k,1,earth[i][j])

mst.sort(key=lambda x: x[2])
p = [i for i in range(num+1)]

def find_set(x):
    return x if p[x] == x else find_set(p[x])

def union(x, y):
    p[find_set(y)] = find_set(x)

def kruskal():
    edges = []
    for edge in mst:
        if find_set(edge[0]) != find_set(edge[1]):
            edges.append(edge)
            union(edge[0], edge[1])
    return edges

edges = kruskal()
for k in edges:
    dist += k[2]
print(dist if dist and len(edges) == num-2 else -1)