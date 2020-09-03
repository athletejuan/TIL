for test_case in range(1,11):
    T,W = map(int, input().split())
    ways = list(input().split())
    wdict = {}
    values = []
    for _ in range(W):
        if ways[0] in wdict:
            wdict[ways.pop(0)].append(ways.pop(0))
        else:
            wdict[ways.pop(0)] = [ways.pop(1)]
    nxt = wdict['0']
    possible = True
    impossible = True
    while possible and impossible:
        after = []
        for i in range(len(nxt)):
            if nxt[i] in wdict:
                after.extend(wdict[nxt[i]])
                if '99' in after:
                    print(f'#{test_case} 1')
                    possible = False
                    break
        else:
            nxt = list(set(after))
            if not after:
                impossible = False
                break
    if not impossible:
        print(f'#{test_case} 0')