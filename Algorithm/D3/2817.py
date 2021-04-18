T = int(input())

for tc in range(1, T+1):
    N,K = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0

    for i in range(1<<N):
        arr = 0
        for j in range(N):
            if i & (1<<j):
                arr += A[j]
                if arr > K:
                    break
        if arr == K:
            cnt += 1
    print('#{} {}'.format(tc, cnt))