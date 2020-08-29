T = int(input())

for _ in range(T):
    x,y = map(int, input().split())
    r = y-x
    a = int(r**.5)
    b = a+1
    if not r**.5-a:
        print(2*a-1)
    elif (r-a**2)/(b**2-a**2)<.5:
        print(2*a)
    else:
        print(2*a+1)