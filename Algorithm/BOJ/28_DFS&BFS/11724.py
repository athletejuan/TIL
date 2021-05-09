import sys
input = sys.stdin.readline

N,M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
base = [[0]*(N+1) for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
cnt = 0

def DFS(i):
    global cnt
    cnt += 1
    stack = [i]
    while stack:
        i = stack.pop()
        for k in range(1, N+1):
            if base[i][k] and not visited[k]:
                stack.append(k)
                base[i][k] = base[k][i] = 0
                visited[k] = 1

for x,y in edges:
    base[x][y] = base[y][x] = 1
for i in range(1, N+1):
    if not visited[i]:
        DFS(i)
print(cnt)