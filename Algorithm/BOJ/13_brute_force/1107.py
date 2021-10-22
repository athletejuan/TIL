N = input()
M = int(input())
working = [1]*10
if M:
    dis = list(map(int, input().split()))
    for i in dis:
        working[i] = 0
move = abs(int(N)-100)

def check(x):
    for i in str(x):
        if not working[int(i)]:
            return False
    return True

click = 500000
for i in range(1000001):
    if check(i) and click > abs(i-int(N))+len(str(i)):
        click = abs(i-int(N))+len(str(i))
if click > move:
    click = move
print(click)











# click = temp = pos = 0
# origin = N
#
# if M < 10:
#     while N:
#         click += 1
#         cnt = 10
#         for i in range(10):
#             if M:
#                 if i not in dis:
#                     if cnt > abs(N%10-i):
#                         cnt = abs(N%10-i)
#                         num = i
#             else:
#                 num = N%10
#         N //= 10
#         temp += num*(10**pos)
#         pos += 1
#         mid = abs(origin-temp)+click if abs(origin-temp)+click < move else move
#     if M:
#         for i in range(1, mid+1):
#             P,M = origin+i, origin-i
#             while P:
#                 if P%10 in dis:
#                     break
#                 P //= 10
#             else:
#                 print(i+click)
#                 break
#             while M:
#                 if M%10 in dis:
#                     break
#                 M //= 10
#             else:
#                 print(i+click)
#                 break
#         else:
#             print(mid)
#     else:
#         print(mid)
# else:
#     print(move)