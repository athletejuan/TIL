T = int(input())

def GCD_LCD(a,b):
    x,y = a,b
    if a > b:
        a,b = b,a
    while a:
        a,b = b%a, a
    print((x*y)//b, b)

for _ in range(T):
    a,b = map(int, input().split())
    GCD_LCD(a,b)