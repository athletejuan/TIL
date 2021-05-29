N,M = map(int, input().split())
origin = []
ps = [[0] * (M+1) for _ in range(N+1)]

for _ in range(N):
    origin.append(list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, M+1):
        ps[i][j] = origin[i-1][j-1] + ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1]

K = int(input())
for k in range(K):
    i,j,x,y = map(int, input().split())
    result = ps[x][y] - ps[i-1][y] - ps[x][j-1] + ps[i-1][j-1]
    print(result)