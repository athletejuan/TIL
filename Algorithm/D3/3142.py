T = int(input())

for test_case in range(1, T+1):
    nums = list(map(int, input().split()))
    a = nums[1]*2 - nums[0]
    b = nums[0] - nums[1]
    print(f'#{test_case} {a} {b}')