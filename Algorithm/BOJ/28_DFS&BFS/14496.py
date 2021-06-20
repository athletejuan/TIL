a,b = map(int, input().split())
N,M = map(int, input().split())
link = [[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)
visited[a] = 1
cnt = 0

def BFS(v):
    global cnt
    while True:
        cnt += 1
        temp = []
        while v:
            x = v.pop()
            for i in range(1, N+1):
                if link[x][i] and not visited[i]:
                    if i == b:
                        print(cnt)
                        return
                    visited[i] = 1
                    temp.append(i)
        v = temp
        if not v:
            print(-1)
            return

for _ in range(M):
    x,y = map(int, input().split())
    link[x][y] = link[y][x] = 1
if a == b:
    print(0)
else:
    BFS([a])