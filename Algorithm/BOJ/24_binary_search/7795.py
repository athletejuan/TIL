T = int(input())

for tc in range(T):
    N,M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    Bset, size = sorted(list(set(B))), {}

    for i in range(M):
        if not size.get(B[i]):
            size[B[i]] = 1
        else:
            size[B[i]] += 1

    pair = dup = 0
    for j in range(len(Bset)-1, -1, -1):
        last, temp = A[N-1], 0
        while last > Bset[j] and N > 0:
            temp += 1
            N -= 1
            last = A[N-1]
        pair += (dup + temp) * size[Bset[j]]
        dup += temp
    print(pair)