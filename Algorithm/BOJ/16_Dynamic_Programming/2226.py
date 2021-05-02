N = int(input())
zeroes = 0

for i in range(1,N):
    if i%2:
        zeroes = zeroes*2 + 1
    else:
        zeroes = zeroes*2 - 1
print(zeroes)

# 재귀 호출(시간 초과)
# def zero_group(x):
#     if x < 2:
#         return x
#     return zero_group(x-2)*2 + zero_group(x-1)
#
# print(zero_group(N-1))