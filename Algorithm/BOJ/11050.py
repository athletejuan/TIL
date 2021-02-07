N,K = list(map(int, input().split()))

start = [1, 1]
for i in range(N-1):
    next_list = [1]
    for j in range(len(start)-1):
        next_list.append(start[j] + start[j+1])
    start = next_list + [1]
print(start[K])


# 재귀
def binomial(N,K):
    if N == 1 or not K or N == K:
        return 1
    else:
        return binomial(N-1, K-1) + binomial(N-1, K)

print(binomial(N,K))