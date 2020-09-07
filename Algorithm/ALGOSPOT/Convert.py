N = int(input())

for t in range(1, N+1):
    wv = input().split()
    if wv[1] == 'kg':
        print('{} {:.4f} lb'.format(t, float(wv[0])*2.2046))
    elif wv[1] == 'lb':
        print('{} {:.4f} kg'.format(t, float(wv[0])*.4536))
    elif wv[1] == 'l':
        print('{} {:.4f} g'.format(t, float(wv[0])*.2642))
    else:
        print('{} {:.4f} l'.format(t, float(wv[0])*3.7854))