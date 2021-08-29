T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ready = [list(map(int, input().split())) for _ in range(N)]
    corridor = [0] * 200
    cnt = 0
    for st in ready:
        if st[0] > st[1]:
            st[0],st[1] = st[1],st[0]
        s, g = (st[0]-1)//2, (st[1]+1)//2
        for i in range(s, g):
            corridor[i] += 1
    for i in corridor:
        if cnt < i:
            cnt = i
    print('#{} {}'.format(tc, cnt))