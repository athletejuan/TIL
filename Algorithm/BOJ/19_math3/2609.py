a,b = map(int, input().split())
m = a*b
while True:
    if a >= b:
        r = a%b
        if not r:
            print(b)
            print(m//b)
            break
        else:
            a = b
            b = r
    else:
        a,b = b,a