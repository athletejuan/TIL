T = int(input())

for test_case in range(1, T+1):
    numbers = input()
    nums = numbers.split()
    if '3' in nums and '1' in nums:
        if nums.index('3'):
            print('A')
        else:
            print('B')
    else:
        if int(nums[0]) > int(nums[1]):
            print('A')
        else:
            print('B')