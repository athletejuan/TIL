T = int(input())

for tc in range(1, T+1):
    N,M = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = sorted(list(map(int, input().split())), reverse=True)
    total = 0
    clist = [0] * 51
    for i in range(N):
        clist[containers[i]] += 1

    for j in range(M):
        limit = trucks[j]
        while limit and not clist[limit]:
            limit -= 1
        clist[limit] -= 1
        total += limit
    print('#{} {}'.format(tc, total))


# 1st_try
# T = int(input())
#
# for tc in range(1, T+1):
#     N,M = map(int, input().split())
#     cons = sorted(list(map(int, input().split())), reverse=True)
#     trucks = sorted(list(map(int, input().split())))
#     total = 0
#
#     while trucks:
#         big = trucks.pop()
#         for i in range(len(cons)):
#             if big >= cons[i]:
#                 total += cons.pop(i)
#                 break
#     print('#{} {}'.format(tc, total))