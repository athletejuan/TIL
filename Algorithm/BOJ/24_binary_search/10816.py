N = input()
cards = input().split()
M = input()
nums = input().split()

many = {}
pick = []

for i in cards:
    if i not in many:
        many[i] = 1
    else:
        many[i] += 1

for j in nums:
    if j in many:
        pick.append(str(many[j]))
    else:
        pick.append('0')
print(' '.join(pick))


# 이분 탐색인데 시간초과..
# import sys
# N = int(sys.stdin.readline())
# cards = list(map(int, sys.stdin.readline().split()))
# cards.sort()
# M = int(sys.stdin.readline())
# nums = list(map(int, sys.stdin.readline().split()))

# exist = []

# for i in range(M):
#     left = 0
#     right = N-1
#     count = 0
#     while left <= right:
#         mid = (left + right) // 2
#         if cards[mid] == nums[i]:
#             count += 1
#             m = mid
#             while 0 < m:
#                 m -= 1
#                 if cards[m] == nums[i]:
#                     count += 1
#                 else:
#                     break
#             while mid < N-1:
#                 mid += 1
#                 if cards[mid] == nums[i]:
#                     count += 1
#                 else:
#                     break
#             break
#         elif cards[mid] < nums[i]:
#             left = mid+1
#         else:
#             right = mid-1
#     exist.append(str(count))
# print(' '.join(exist))