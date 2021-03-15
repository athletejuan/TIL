C,R = map(int, input().split())
K = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if K > C*R:
    print(0)
else:
    hall = [[0] * C for _ in range(R)]
    x,y = R-1,0
    cnt, way = 1, 0
    hall[x][y] = cnt
    while cnt < K:
        a,b = x + dx[way%4], y + dy[way%4]
        if 0 <= a < R and 0 <= b < C and not hall[a][b]:
            cnt += 1
            hall[a][b] = cnt
            x,y = a,b
        else:
            way += 1
    print(y+1, R-x)