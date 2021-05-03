N,K = map(int, input().split())
check = [1, 1] + [0] * (N-1)

def Eratosthenes():
    count = 0
    for i in range(2, N+1):
        if not check[i]:
            n = 1
            while i*n <= N:
                if not check[i*n]:
                    check[i*n] = 1
                    count += 1
                    if count == K:
                        return i*n
                n += 1

print(Eratosthenes())