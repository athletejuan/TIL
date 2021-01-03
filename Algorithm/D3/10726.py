T = int(input())

for test_case in range(1, T+1):
    N,M = map(int, input().split())
    if M >= 2**N-1:
        for _ in range(N):
            re = M%2
            if not re:
                print(f'#{test_case} OFF')
                break
            M//=2
        else:
            print(f'#{test_case} ON')
    else:
        print(f'#{test_case} OFF')