def exchangee():
    for i in range(1, 8):
        for j in range(15-i):
            if n == sum(days[j:j+i]):
                return i


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    days = list(map(int, input().split()))
    one = 0
    for day in days:
        one += day
    days += days

    div = (n-1) // one
    cnt = div*7
    n -= (one*div)
    cnt += exchangee()
    print('#{} {}'.format(tc, cnt))