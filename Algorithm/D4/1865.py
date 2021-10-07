def success(idx, percent):
    global best
    if idx == N:
        best = percent
    else:
        if percent <= best:
            return
        for i in range(idx, N):
            used[idx], used[i] = used[i], used[idx]
            now = percent * ability[idx][used[idx]]
            if now > best:
                success(idx+1, now)
            used[idx], used[i] = used[i], used[idx]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ability = [list(map(lambda x: int(x)/100, input().split())) for _ in range(N)]
    used = [i for i in range(N)]
    best = 0
    success(0, 1)

    print('#{} {:.6f}'.format(tc, best*100))