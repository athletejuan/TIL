X,Y = map(int, input().split())

win = (Y*100)//X
if Y >= X*.99:
    print(-1)
else:
    low, high = 1, X
    while low <= high:
        mid = (low+high)//2
        game = (Y+mid)*100//(X+mid)
        if game > win:
            high = mid-1
        else:
            low = mid+1
    print(high+1)