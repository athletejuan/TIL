T = int(input())

for _ in range(T):
    a,b = map(int, input().split())
    a %= 10
    r = a%5
    if not r or r == 1:
        if not a:
            print(10)
        else:
            print(a)
    elif 1 < r < 4:
        if b%4:
            print((a**(b%4))%10)
        else:
            print((a**4)%10)
    else:
        if b%2:
            print(a)
        else:
            print((a**2)%10)