N = int(input())

for tc in range(N):
    r,e,c = map(int, input().split())

    if e-c > r:
        print('advertise')
    elif e-c < r:
        print('do not advertise')
    else:
        print('does not matter')