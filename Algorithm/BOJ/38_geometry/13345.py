points = [list(map(int, input().split())) for _ in range(3)]
check = []
for i in range(2):
    dist = (points[i][0] - points[i+1][0])**2 + (points[i][1] - points[i+1][1])**2
    if not check or dist != check[0]:
        check.append(dist)
if len(check) == 1:
    for j in range(2):
        print(points[0][j] + points[2][j] - points[1][j], end=" ")
else:
    if (points[0][0] - points[2][0])**2 + (points[0][1] - points[2][1])**2 == check[0]:
        for j in range(2):
            print(points[1][j] + points[2][j] - points[0][j], end=" ")
    else:
        for j in range(2):
            print(points[0][j] + points[1][j] - points[2][j], end=" ")