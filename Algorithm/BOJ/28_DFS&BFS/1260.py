N,M,V = map(int, input().split())

def DFS(V):
    print(V, end=' ')
    visit[V] = 1
    for i in range(1, N+1):
        if base[V][i] and not visit[i]:
            DFS(i)

def BFS(V):
    queue = [V]
    while queue:
        V = queue.pop(0)
        print(V, end=' ')
        visit[V] = 0
        for i in range(1, N+1):
            if base[V][i] and visit[i]:
                queue.append(i)
                visit[i] = 0

base = [[0]*(N+1) for _ in range(N+1)]
visit = [0 for _ in range(N+1)]
for _ in range(M):
    x,y = map(int, input().split())
    base[x][y] = base[y][x] = 1

DFS(V)
print()
BFS(V)