T = int(input())

for tc in range(1, T+1):
    N = float(input())
    binary = ''

    for i in range(1, 13):
        if N >= 2**-i:
            binary += '1'
            N -= 2**-i
        else:
            binary += '0'
        if not N:
            print('#{} {}'.format(tc, binary))
            break
    else:
        print('#{} overflow'.format(tc))