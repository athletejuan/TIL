T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    points = []
    for i in range(N):
        points.append(list(map(int, input().split())))
    cnt = 0
    for j in range(N):
        for k in range(N):
            if points[j][0] < points[k][0] and points[j][1] > points[k][1]:
                cnt += 1
            elif points[j][0] > points[k][0] and points[j][1] < points[k][1]:
                cnt += 1
    print(f'#{test_case} {int(cnt/2)}')