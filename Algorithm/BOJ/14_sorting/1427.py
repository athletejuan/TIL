N = input()
nums = []

for n in N:
    nums.append(int(n))
    
    for i in range(len(nums)-2, -1, -1):
        while nums[i] < int(n):
            nums[i+1] = nums[i]
            nums[i] = int(n)
print(''.join(map(str, nums)))