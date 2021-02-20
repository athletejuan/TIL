T = int(input())

for _ in range(T):
    c,v = map(int, input().split())
    print('You get {} piece(s) and your dad gets {} piece(s).'.format(c//v, c%v))