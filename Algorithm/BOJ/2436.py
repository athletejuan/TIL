G,L = map(int, input().split())

for i in range(int((L//G)**.5), 0, -1):
    if not (L//G)%i:
        A = (L//G)//i
        B = i
        while B:
            if A < B:
                A,B = B,A 
            A,B = B,A-B
        if A == 1:
            print(i*G,L//i)
            break 