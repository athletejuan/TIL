K = int(input())
buildings = list(map(int, input().split()))

for i in range(K):
    start = ((2**K)-1)//(2**(i+1))
    now = ''
    while (2**K)-1 > start:
        now += str(buildings[start]) + ' '
        start += 2**(K-i)
    print(now)