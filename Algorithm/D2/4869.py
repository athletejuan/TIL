T = int(input())

for tc in range(1, T+1):
    N = int(input())
    p = 1
    t = N//10
    for i in range(1, t+1):
        if i%2:
            p = (p*2) - 1
        else:
            p = (p*2) + 1
    print(f'#{tc} {p}')


# memoization(more fast)
# T = int(input())
# Ns = []
# max_N = 0
# for _ in range(T):
#     N = int(input())
#     Ns.append(N//10)
#     if N//10 > max_N:
#         max_N = N//10

# t = max_N
# memo = [1] + [0] * (t-1)
# for i in range(1, t):
#     if i%2:
#         memo[i] = (memo[i-1]*2) + 1
#     else:
#         memo[i] = (memo[i-1]*2) - 1

# for idx,j in enumerate(Ns):
#     print('#{} {}'.format(idx+1, memo[j-1]))