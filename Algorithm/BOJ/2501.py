N,K = map(int, input().split())
cnt = 0

for n in range(1, N+1):
    if not N%n:
        cnt += 1
        if cnt == K:
            print(n)
            break
else:
    print(0)