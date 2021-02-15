T = int(input())

arr = [i for i in range(1, 13)]
for tc in range(1, T+1):
    N,K = map(int, input().split())
    cnt = 0
    for i in range(1 << 12):
        sub = []
        for j in range(12):
            if i & (1 << j):
                sub.append(arr[j])
        if len(sub) == N and sum(sub) == K:
            cnt += 1
    print(f'#{tc} {cnt}')