N = int(input())
r = list(map(int, input().split()))
M = int(input())
r.sort()
if sum(r) <= M:
   print(r[-1])
else:
    for i in range(N):
        if r[i] > M//(N-i):
            print(M//(N-i))
            break
        else:
            M -= r[i]

# 이분 탐색
# low, high = 0, max(r)
# while low <= high:
#     mid = (low + high) // 2
#     num = 0
#     for i in r:
#         if i >= mid: 
#             num += mid
#         else: 
#             num += i
#     if num <= M: 
#         low = mid + 1
#     else: 
#         high = mid - 1
# print(high)