import sys
input = sys.stdin.readline

N = int(input())
nums = {}

for i in range(N):
    num = int(input())
    if num in nums:
        nums[num] += 1
    else:
        nums[num] = 1
for k,v in sorted(nums.items()):
    if v:
        for _ in range(v):
            print(k)