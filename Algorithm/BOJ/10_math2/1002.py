T = int(input())

for t in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif x1 == x2 and y1 == y2 and r1 != r2:
        print(0)
    elif ((x2 - x1)**2 + (y2 - y1)**2)**.5 == (r1 + r2) or (((x2 - x1)**2 + (y2 - y1)**2)**.5 + min(r1, r2)) == max(r1, r2):
        print(1)
    elif ((x2 - x1)**2 + (y2 - y1)**2)**.5 < (r1 + r2) and (((x2 - x1)**2 + (y2 - y1)**2)**.5 + min(r1, r2)) > max(r1, r2):
        print(2)
    else:
        print(0)