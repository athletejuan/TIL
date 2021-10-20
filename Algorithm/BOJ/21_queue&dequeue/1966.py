T = int(input())

for tc in range(T):
    N,M = map(int, input().split())
    Q = list(map(int, input().split()))
    count = 0
    breaker = False
    for i in range(N):
        for idx, j in enumerate(Q):
            if j == max(Q):
                count += 1
                if M == idx:
                    print(count)
                    breaker = True
                elif M > idx:
                    M -= (idx+1)
                else:
                    M += len(Q[idx+1:])
                Q = Q[idx+1:] + Q[:idx]
                break
        if breaker:
            break