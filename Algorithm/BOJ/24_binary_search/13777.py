while True:
    num = int(input())
    if not num:
        break
    L,R = 1,50
    while L <= R:
        mid = (L+R)//2
        if num < mid:
            R = mid - 1
        elif mid == num:
            print(mid)
            break
        else:
            L = mid + 1
        print(mid, end=' ')