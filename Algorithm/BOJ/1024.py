N,L = map(int, input().split())
array = []
for i in range(L, 101):
    h = i//2
    if N > 6 and i > N//2:
        print(-1)
        break
    if not i%2:
        if not N%h and 2*((N//h)//2)+1 == N//h and (N//h+1)//2 - h >= 0:
            a = -h
            for j in range(i):
                a += 1
                array.append(str((N//h)//2 + a))
            print(' '.join(array))
            break
    else:
        if not N%i and (N//i +h+1-i) >= 0:
            for j in range(i):
                array.append(str(N//i +j-h))
            print(' '.join(array))
            break
else:
    print(-1)