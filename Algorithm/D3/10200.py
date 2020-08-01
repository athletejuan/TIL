T = int(input())

for test_case in range(1, T+1):
    N, A, B = map(int, input().split())
    if A+B-N > 0:
        print(f'#{test_case} {min(A,B)} {A+B-N}')
    else:
        print(f'#{test_case} {min(A,B)} 0')