T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    X = N**(1/3)
    I = round(X)
    if abs(I-X) < 1e-9:
        print(f'#{test_case} {I}')
    else:
        print(f'#{test_case} -1')