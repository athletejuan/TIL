N,M = map(int, input().split())

N = N%M
total = cut = 0
while N:
    N,M,cut = N%(M-N*((M-1)//N)), M-N*((M-1)//N), N*((M-1)//N)
    total += cut
print(total)


# 재귀
# def GDS(a, b):
#     if a%b == 0:
#         return b
#     return GDS(b, a%b)
#
#
# N, M = map(int, input().split())
# print(M - GDS(N, M))