T = int(input())

for _ in range(T):
    N,M = map(int, input().split())
    cnt = 0
    for num in range(N,M+1):
        for n in str(num):
            if n == '0':
                cnt += 1
    print(cnt)