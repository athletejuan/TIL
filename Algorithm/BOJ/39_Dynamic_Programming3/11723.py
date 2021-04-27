# 출제의도는 비트마스크 활용

import sys
input = sys.stdin.readline
M = int(input())
eset = [0]*21

for _ in range(M):
    oper = input().split()
    if oper[0] == 'add':
        eset[int(oper[1])] = 1
    elif oper[0] == 'remove':
        eset[int(oper[1])] = 0
    elif oper[0] == 'check':
        print(1 if eset[int(oper[1])] else 0)
    elif oper[0] == 'toggle':
        eset[int(oper[1])] = 0 if eset[int(oper[1])] else 1
    elif oper[0] == 'all':
        eset = [1]*21
    else:
        eset = [0]*21


# 71% 시간초과
# import sys
# input = sys.stdin.readline

# M = int(input())
# eset = set()
# for _ in range(M):
#     cal = input().split()
#     if cal[0] == 'add':
#         eset.add(cal[1])
#     elif cal[0] == 'remove':
#         eset.discard(cal[1])
#     elif cal[0] == 'check':
#         print(1 if cal[1] in eset else 0)
#     elif cal[0] == 'toggle':
#         if cal[1] in eset:
#             eset.remove(cal[1])
#         else:
#             eset.add(cal[1])
#     elif cal[0] == 'all':
#         eset = set(str(i) for i in range(1, 21))
#     else:
#         eset = set()