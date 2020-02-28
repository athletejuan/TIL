T = int(input())

for test_case in range(1, T+1):
    nums = list(map(int, input().split()))
    for i in nums:
        if nums.count(i)%2:
            print(f'#{test_case} {i}')
            break