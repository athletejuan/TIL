T = int(input())

for test_case in range(1, T+1):
    N, M = int(input()), list(map(int, input().split()))
    ans = ' '.join(map(str, sorted(M)))
    print(f'#{test_case} {ans}')