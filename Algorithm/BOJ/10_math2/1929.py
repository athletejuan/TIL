M,N = map(int, input().split())
a = [False, False] + [True]*(N-1)
prime = []

for i in range(2, N+1):
    if a[i]:
        for j in range(2*i, N+1, i):
            a[j] = False
        if i >= M:
            prime.append(i)
for k in prime:
    print(k)