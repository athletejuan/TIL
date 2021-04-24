for tc in range(1,11):
    N = int(input())
    origin = list(input().split())
    C = int(input())
    command = list(input().split(' I '))
    for i in range(C):
        if not i:
            pw = list(command[i][2:].split())
        else:
            pw = list(command[i].split())
        if int(pw[0]) < 11:
            origin = origin[:int(pw[0])] + pw[2:] + origin[int(pw[0]):]
    print('#{} {}'.format(tc, ' '.join(origin[:10])))