n = int(input())
dp = [0] * (n+1)

def handshake():
    i = 0
    while i < n:
        i += 1
        if i < 3:
            dp[i] = i
        else:
            dp[i] = (dp[i-1] + dp[i-2])%10

handshake()
print(dp[n])