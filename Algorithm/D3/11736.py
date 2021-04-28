T = int(input())

for tc in range(1, T+1):
    N = int(input())
    P = list(map(int, input().split()))
    cnt = 0
    for i in range(N-2):
        if (P[i+1]-P[i])*(P[i+1]-P[i+2]) < 0:
            cnt += 1
    print('#{} {}'.format(tc, cnt))