def printer(M, Q):
    count = 0
    while True:
        for idx, j in enumerate(Q):
            if j == max(Q):
                count += 1
                if M == idx:
                    return count
                elif M > idx:
                    M -= (idx+1)
                else:
                    M += len(Q[idx+1:])
                Q = Q[idx+1:] + Q[:idx]
                break


T = int(input())
for tc in range(T):
    N,M = map(int, input().split())
    Q = list(map(int, input().split()))
    print(printer(M, Q))