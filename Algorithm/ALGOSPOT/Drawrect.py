T = int(input())

for t in range(T):
    points = []
    for _ in range(3):
        points.append(list(map(int, input().split())))
    x,y = [],[]
    for point in points:
        x.append(point[0])
        y.append(point[1])
    last = []
    for a in x:
        if x.count(a) == 1:
            last.append(str(a))
    for b in y:
        if y.count(b) == 1:
            last.append(str(b))
    print(' '.join(last))