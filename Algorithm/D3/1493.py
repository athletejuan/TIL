T = int(input())

for tc in range(1, T+1):
    p,q = map(int, input().split())
    a = b = num = 0
    plus = 1

    while True:
        num += plus
        plus += 1
        if not a and num >= p:
            a,ap = plus,num-p
        if not b and num >= q:
            b,bp = plus,num-q
        if a and b:
            c = a+b
            if plus == c:
                print('#{} {}'.format(tc, num-(ap+bp+1)))
                break