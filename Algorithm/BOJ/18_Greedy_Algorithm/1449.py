N,L = map(int, input().split())
leaks = sorted(list(map(int, input().split())))
cnt = 1

while leaks:
    tape = leaks[0]+L-1
    for idx,l in enumerate(leaks):
        if l > tape:
            leaks = leaks[idx:]
            break
    else:
        print(cnt)
        break
    cnt += 1