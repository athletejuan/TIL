nums = [int(input()) for _ in range(5)]
total = 0
for num in nums:
    total += num
print(total//5)

for i in range(4):
    for j in range(i,5):
        if nums[i] > nums[j]:
            nums[i],nums[j] = nums[j],nums[i]
print(nums[2])