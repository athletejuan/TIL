T = int(input())

for _ in range(T):
    n = int(input())
    a = 1
    d = 1
    while d <= n:
        a += 1
        d = a**2
    print(a-1)