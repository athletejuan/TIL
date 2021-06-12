N = int(input())
A = list(map(int, input().split()))
dp = [[1] for _ in range(N)]
max_dp = 1

for i in range(N):
    dp[i].append(A[i])
    for j in range(i):
        if A[i] > dp[j][1] and dp[i][0] == dp[j][0]:
            dp[i][0] = dp[j][0] + 1
            if dp[i][0] > max_dp:
                max_dp = dp[i][0]
print(max_dp)