T = int(input())

for test_case in range(1, T+1):
    N,M = map(int, input().split())
    reg = []
    for _ in range(N):
        reg.append(list(map(int, input().split())))
    kl = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            kill = 0
            for k in range(M):
                for l in range(M):
                    kill += reg[j+k][i+l]
            kl.append(kill)
    print(f'#{test_case} {max(kl)}')