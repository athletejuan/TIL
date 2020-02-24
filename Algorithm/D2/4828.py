T = int(input())

for test_case in range(1, T+1):
    num = input()
    nums = list(map(int, input().split()))
    sn = sorted(nums)
    print(f'#{test_case} {sn[-1] - sn[0]}')