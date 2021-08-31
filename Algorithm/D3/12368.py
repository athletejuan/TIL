T = int(input())

for tc in range(1, T+1):
    A,B = map(int, input().split())
    print('#{} {}'.format(tc, (A+B)%24))