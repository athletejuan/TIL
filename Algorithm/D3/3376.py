T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    start = [1,1,1]
    if N < 4:
        print(f'#{test_case} 1')
    for i in range(N-3):
        start.append(start[-3]+start[-2])
    print(start)
    print(f'#{test_case} {start[-1]}')