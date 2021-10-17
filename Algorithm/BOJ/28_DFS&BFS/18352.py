import sys
input = sys.stdin.readline

N,M,K,X = map(int, input().split())
tree = [[] for _ in range(N+1)]
for _ in range(M):
    A,B = map(int, input().split())
    tree[A].append(B)

visited = [0] * (N+1)
visited[X] = -1
cnt = 1

queue, temp, cities = tree[X], [], []
while True:
    while queue:
        v = queue.pop(0)
        if not visited[v]:
            temp += tree[v]
            visited[v] = cnt
            if visited[v] == K:
                cities.append(v)
    if K == cnt:
        break
    cnt += 1
    queue, temp = temp, []

if cities:
    for city in sorted(cities):
        print(city)
else:
    print(-1)