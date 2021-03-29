N = int(input())
dp = [0] * (N+1)

def tile():
    i = 0
    while i < N:
        i += 1
        if i < 3:
            dp[i] = i
        else:
            dp[i] = (dp[i-1] + dp[i-2])%15746

tile()
print(dp[N])