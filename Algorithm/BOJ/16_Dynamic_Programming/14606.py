N = int(input())

enjoy = 0
for i in range(1, N):
    enjoy += i
print(enjoy)

# DP
dp = [0] * (N+1)
def enjoy(N):
    if N == 1:
        return 0
    if N == 2:
        return 1
    dp[N] = (N//2)*(N-(N//2)) + enjoy(N//2) + enjoy(N-(N//2))
    return dp[N]

print(enjoy(N))