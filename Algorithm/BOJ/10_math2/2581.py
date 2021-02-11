M = int(input())
N = int(input())

prime = 0
era = [0,0] + [1]*(N-1)
for i in range(2, N+1):
    n = 1
    if era[i]:
        if i >= M:
            if not prime:
                first = i
            prime += i
        while i*n <= N:
            era[i*n] = 0
            n += 1
if prime:
    print(prime)
    print(first)
else:
    print(-1)