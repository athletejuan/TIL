T = int(input())

for test_case in range(1, T+1):
    numbers = input()
    nums = numbers.split()
    a = int(nums[0]) // int(nums[1])
    b = int(nums[0]) % int(nums[1])
    print(f'#{test_case} {a} {b}')