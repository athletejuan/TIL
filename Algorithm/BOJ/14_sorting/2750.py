N = int(input())
nums = []

for _ in range(N):
    key = int(input())
    nums.append(key)

    for i in range(len(nums)-2, -1, -1):
        if nums[i] > key:
            nums[i+1] = nums[i]
            nums[i] = key

for i in nums:
    print(i)


# for _ in range(N):
#     nums.append(int(input()))

# for i in range(N):
#     key = nums[i]
#     j = i - 1

#     while j >= 0 and nums[j] > key:
#         nums[j+1] = nums[j]
#         j -= 1
#     nums[j+1] = key
# for i in nums:
#     print(i)