T = int(input())

def DFS(x, length):
    global max_length, visited
    visited[x] = 1
    for j in range(1, N+1):
        if base[x][j] and not visited[j]:
            DFS(j, length+1)
            visited[j] = 0
    visited[x] = 0
    if max_length < length:
        max_length = length

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    base = [[0] * (N+1) for _ in range(N+1)]
    visited = [0] * (N+1)
    max_length = 1
    for edge in edges:
        base[edge[0]][edge[1]] = base[edge[1]][edge[0]] = 1
    for i in range(1, N+1):
        for j in range(1, N+1):
            if base[i][j]:
                DFS(i, 1)
    print('#{} {}'.format(tc, max_length))