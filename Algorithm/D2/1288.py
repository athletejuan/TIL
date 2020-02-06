T = int(input())

for test_case in range(1, T+1):
    number = input()
    j = 1
    nums = []
    while True:
        multi_number = int(number) * j
        for i in str(multi_number):
            if i not in nums:
                nums.append(i)
        j += 1
        if len(nums) == 10:
            print(multi_number)
            break