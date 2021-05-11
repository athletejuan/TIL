T = int(input())

for tc in range(1, T+1):
    D,N = map(int, input().split())
    horses = [list(map(int, input().split())) for i in range(N)]
    time = 0
    for i in range(N):
        if time < (D - horses[i][0]) / horses[i][1]:
            time = (D - horses[i][0]) / horses[i][1]
    print('#{} {:.20g}'.format(tc, D/time))