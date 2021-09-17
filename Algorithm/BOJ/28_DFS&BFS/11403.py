N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
route = [[0]*N for _ in range(N)]

for i in range(N):
    visited = [0]*N
    stack = [i]
    while stack:
        s = stack.pop()
        for j in range(N):
            if G[s][j] and not visited[j]:
                route[i][j] = 1
                visited[j] = 1
                stack.append(j)
    print(*route[i])