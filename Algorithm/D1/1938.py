T = int(input())

for test_case in range(1, T+1):
    numbers = input()
    nums = numbers.split()
    print(int(nums[0])+ int(nums[1]))
    print(int(nums[0]) - int(nums[1]))
    print(int(nums[0]) * int(nums[1]))
    print(int(nums[0]) // int(nums[1]))
