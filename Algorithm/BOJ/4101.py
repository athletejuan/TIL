while True:
    A,B = map(int, input().split())
    if not A:
        break
    if A > B:
        print('Yes')
    else:
        print('No')