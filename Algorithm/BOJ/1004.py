T = int(input())

for t in range(T):
    sx, sy, ex, ey = map(int, input().split())
    n = int(input())
    count = 0
    for _ in range(n):
        x, y, r = map(int, input().split())
        if (sx-x)**2 + (sy-y)**2 < r**2 and (ex-x)**2 + (ey-y)**2 > r**2:
            count += 1
        elif (ex-x)**2 + (ey-y)**2 < r**2 and (sx-x)**2 + (sy-y)**2 > r**2:
            count += 1
    print(count)