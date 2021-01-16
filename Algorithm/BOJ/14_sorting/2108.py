import sys
from collections import Counter

N = int(sys.stdin.readline())
# N = int(input())
nums = []

for _ in range(N):
    nums.append(int(sys.stdin.readline()))
    # nums.append(int(input()))

nums.sort()
mc = Counter(nums).most_common()
# one = sorted(list(set(nums)))
# c = 0
# for i in one:
#     if nums.count(i) > c:
#         c = nums.count(i)
#         many = []
#         many.append(i)
#     elif nums.count(i) == c:
#         many.append(i)

print(round(sum(nums)/N))
print(nums[N//2])
if len(mc) > 1 and mc[0][1] == mc[1][1]:
    print(mc[1][0])
else:
    print(mc[0][0])    
# if len(many) > 1:
#     print(many[1])
# else:
#     print(many[0])
print(nums[-1]-nums[0])