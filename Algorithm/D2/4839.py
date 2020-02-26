T = int(input())

for test_case in range(1, T+1):
    P,A,B = map(int, input().split())
    cA = 0
    cB = 0
    c = int((P+1)/2)
    l, r = 1, P
    while c != A:
        if c < A:
            l = c
        else:
            r = c
        c = int((l+r)/2)
        cA += 1
    c = int((P+1)/2)
    l, r = 1, P
    while c != B:
        if c < B:
            l = c
        else:
            r = c
        c = int((l+r)/2)
        cB += 1
    if cA < cB:
        print(f'#{test_case} A')
    elif cA > cB:
        print(f'#{test_case} B')
    else:
        print(f'#{test_case} 0')