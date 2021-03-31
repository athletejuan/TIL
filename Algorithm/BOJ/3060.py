T = int(input())

for _ in range(T):
    N = int(input())
    day = sum(list(map(int, input().split())))
    cnt = 1
    while N >= day:
        cnt += 1
        day *= 4
    print(cnt)