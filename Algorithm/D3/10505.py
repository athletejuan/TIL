T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    test = list(map(int, input().split()))
    ave = sum(test)/N
    cnt = 0
    for i in test:
        if i - ave <= 0:
            cnt += 1
    print(f'#{test_case} {cnt}')