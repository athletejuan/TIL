N,K = map(int, input().split())
num = list(input())
big, cnt = [], 0
for i in range(N):
    while big and num[i] > big[-1] and cnt < K:
        big.pop()
        cnt += 1
    big.append(num[i])
print(''.join(big[:N-K]))


#1st try
# N,K = map(int, input().split())
# num = list(input())
# find = sorted(num, reverse=True)[N-K]
# cnt = 0
# result = ''
# temp = ''
# breaker = True
# for idx, i in enumerate(num):
#     if cnt == K:
#         result += temp + ''.join(num[idx:])
#         break
#     if i > find:
#         if breaker:
#             if temp:
#                 if temp[-1] < str(i):
#                     cnt += len(temp)
#                     temp = str(i)
#                 else:
#                     if cnt + len(temp) == K:
#                         breaker = False
#                         break
#                     temp += str(i)
#             else:
#                 temp = str(i)
#     else:
#         cnt += 1
# else:
#     result = temp
# print(result)


# 2nd try
# for i in range(K):
#     for j in range(N-1):
#         if num[j] < num[j+1]:
#             num.pop(j)
#             N -= 1
#             break
#     else:
#         print(''.join(num[:-(K-i)]))
#         break
# else:
#     print(''.join(num))