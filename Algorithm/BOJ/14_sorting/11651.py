N = int(input())

points = []
for _ in range(N):
    point = list(map(int,input().split()))
    points.append([point[1], point[0]])

spoints = sorted(points)
for i in range(N):
    print(str(spoints[i][1]) + ' ' + str(spoints[i][0]))