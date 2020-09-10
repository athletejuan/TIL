while True:
    n = int(input())
    if not n:
        break
    check = [False, False] + [True]*(2*n-1)
    prime = []
    cnt = 0
    for i in range(1, 2*n+1):
        if check[i]:
            prime.append(i)
            for j in range(2*i, 2*n+1, i):
                check[j] = False
    for k in prime:
        if k > n:
            cnt += 1
    print(cnt)