N = int(input())
dp = [0] * (N+1)
i = 1

def pinary(N):
    if N < 2:
        dp[N] = N
    return dp[N]

if N < 2:
    print(N)
else:
    while i < N:
        i += 1
        dp[i] = pinary(i-1) + pinary(i-2)
    print(dp[i])