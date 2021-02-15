T = int(input())

for tc in range(1, T+1):
    P,Pa,Pb = map(int, input().split())
    A,B = 0,0
    L,R = 1,P
    while L <= R:
        mid = (L+R)//2
        A += 1
        if mid == Pa:
            break
        elif mid > Pa:
            R = mid-1
        else:
            L = mid+1
    L,R = 1,P
    while L <= R:
        mid = (L+R)//2
        B += 1
        if mid == Pb:
            if A < B:
                print(f'#{tc} A')
                break
            elif A > B:
                print(f'#{tc} B')
                break
            else:
                print(f'#{tc} 0')
                break
        elif mid > Pb:
            R = mid-1
        else:
            L = mid+1