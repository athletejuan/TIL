N,M = map(int, input().split())
base = [input() for _ in range(N)]

def rectangular(l):
    while l:
        for i in range(M-l):
            for j in range(N-l):
                if base[j][i] == base[j][i+l] == base[j+l][i] == base[j+l][i+l]:
                    return (l+1)**2
        return rectangular(l-1)
    return 1

l = N-1 if N < M else M-1

print(rectangular(l))


# 1st try
# breaker = False

# if N < M:
#     for i in range(N-1):
#         for j in range(i+1):
#             for k in range(M-N+i+1):
#                 if r[j][k] == r[j][k+N-1-i] == r[j+N-1-i][k] == r[j+N-1-i][k+N-1-i]:
#                     print((N-i)**2)
#                     breaker = True
#                     break
#             if breaker:
#                 break
#         if breaker:
#             break
# else:
#     for i in range(M-1):
#         for j in range(i+1):
#             for k in range(N-M+i+1):
#                 if r[k][j] == r[k][j+M-1-i] == r[k+M-1-i][j] == r[k+M-1-i][j+M-1-i]:
#                     print((M-i)**2)
#                     breaker = True
#                     break
#             if breaker:
#                 break
#         if breaker:
#             break
# if not breaker:
#     print(1)