from collections import deque

N,K = map(int, input().split())
visited = [0]*100001
queue = deque()
queue.append([N,0])

while queue:
    N = queue.popleft()
    if N[0] == K:
        print(N[1])
        break
    visited[N[0]] = 1
    if 2 * N[0] < 100001 and not visited[2*N[0]]:
        queue.append([2*N[0], N[1]+1])
    if N[0] < 100000 and not visited[N[0]+1]:
        queue.append([N[0]+1, N[1]+1])
    if N[0] > 0 and not visited[N[0]-1]:
        queue.append([N[0]-1, N[1]+1])