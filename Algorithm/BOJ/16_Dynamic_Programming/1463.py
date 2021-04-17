N = int(input())
dp = [[] for _ in range(100)]
dp[0].append(N)
cnt = 0

def one():
    global cnt
    while True:
        for num in dp[cnt]:
            if num == 3 or num == 2:
                return cnt+1
            if not num % 3:
                dp[cnt+1].append(num // 3)
            if not num % 2:
                dp[cnt+1].append(num // 2)
            dp[cnt+1].append(num-1)
        cnt += 1

print(0 if N == 1 else one())