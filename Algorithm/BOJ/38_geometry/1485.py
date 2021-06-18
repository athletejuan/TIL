T = int(input())

points = []
for _ in range(T):
    points = [list(map(int, input().split())) for i in range(4)]
    dist, linear = [], []
    for j in range(1, 4):
        dist.append([(points[0][0] - points[j][0])**2 + (points[0][1] - points[j][1])**2, j])
        if points[0][1] - points[j][1]:
            line = (points[0][0] - points[j][0])/(points[0][1] - points[j][1])
        else:
            line = 'inf'
        if not linear:
            linear.append(line)
        else:
            if line in linear:
                print(0)
                break
    else:
        dist.sort()
        #1. (사각형 여부 확인) 한 꼭지점 기준 양쪽 꼭지점의 x,y좌표를 더했을때 대각선 방향 꼭지점 좌표
        #2. (정사각형 여부 확인) 한 꼭지점 기준 인접 꼭지점과의 거리 제곱의 2배가 대각선 꼭지점과의 거리와 같은지
        if points[dist[0][1]][0] + points[dist[1][1]][0] - points[0][0] == points[dist[2][1]][0] and points[dist[0][1]][1] + points[dist[1][1]][1] - points[0][1] == points[dist[2][1]][1] and 2*((points[dist[0][1]][0] - points[0][0])**2 + (points[dist[0][1]][1] - points[0][1])**2) == (points[dist[2][1]][0] - points[0][0])**2 + (points[dist[2][1]][1] - points[0][1])**2:
            print(1)
        else:
            print(0)