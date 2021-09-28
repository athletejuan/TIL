T = int(input())

for tc in range(1, T+1):
    N,M = map(int, input().split())
    status = 'OFF'
    while M and N:
        M,R = divmod(M,2)
        if not R:
            break
        N -= 1
    if not N:
        status = 'ON'

    print('#{} {}'.format(tc, status))