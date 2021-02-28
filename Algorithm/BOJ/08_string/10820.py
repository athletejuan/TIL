while True:
    try:
        text = list(input())
        l,u,n,s = 0,0,0,0
        if not text:
            break
        for c in text:
            if ord(c) > 96:
                l += 1
            elif ord(c) > 64:
                u += 1
            elif ord(c) > 46:
                n += 1
            else:
                s += 1
        print('{} {} {} {}'.format(l,u,n,s))
    except EOFError:
        break