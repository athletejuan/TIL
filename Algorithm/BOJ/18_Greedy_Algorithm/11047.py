N,K = map(int, input().split())

coins = []
cnt = 0
for _ in range(N):
    coin = int(input())
    coins.append(coin)

for i in sorted(coins, reverse=True):
    if i <= K:
        cnt += K//i
        K = K%i
    elif not K:
        break
print(cnt)