T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    if N%2:
        S1 = N*((N//2)+1)
    else:
        S1 = (N+1)*(N//2)
    print(f'#{test_case} {S1} {(S1*2)-N} {S1*2}')