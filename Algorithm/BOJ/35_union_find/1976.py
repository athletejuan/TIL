def DFS(s):
    connect = [s]
    while connect:
        s = connect.pop()
        for i in range(N):
            if adj[s][i] and not visited[i]:
                visited[i] = 1
                connect.append(i)


N = int(input())
M = int(input())
adj = [list(map(int, input().split())) for _ in range(N)]
trip = list(map(int, input().split()))
start = trip[0]
visited = [0] * N
visited[start-1] = 1

DFS(start-1)
for c in range(M):
    if not visited[trip[c]-1]:
        print('NO')
        break
else:
    print('YES')