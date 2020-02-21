T = int(input())

for test_case in range(1, T+1):
    wtf = list(map(int, input().split()))
    tear = wtf[2] + ((wtf[1] + ((wtf[0] - 11) * 24) - 11) * 60) - 11
    if tear < 0:
        tear = -1
    print(f'#{test_case} {tear}')