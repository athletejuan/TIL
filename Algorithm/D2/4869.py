T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    p = 1
    t = N//10
    for i in range(1, t+1):
        if i%2:
            p = (p*2) - 1
        else:
            p = (p*2) + 1
    print(f'#{test_case} {p}')