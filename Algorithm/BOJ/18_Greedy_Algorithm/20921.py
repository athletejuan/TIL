N,K = map(int, input().split())

for i in range(N):
    if N-1-i > K:
        break
    K -= (N-1-i)
temp = list(map(str, range(1, N-i+1)))
some = list(map(str, range(N, 0, -1)))[:i] + [temp.pop(K)] + temp
print(' '.join(some))