N = int(input())

points = []
for _ in range(N):
    points.append(list(map(int,input().split())))

spoints = sorted(points)
for i in range(N):
    print(str(spoints[i][0]) + ' ' + str(spoints[i][1]))