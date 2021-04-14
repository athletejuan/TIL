T = int(input())

def backtrack(now):
    global cnt
    stop, charge = now, BS[now]
    cnt += 1
    for i in range(now, now+BS[now]+1):
        if i + BS[i] > charge:
            stop, charge = i, i + BS[i]
        if charge >= N-1:
            return
    else:
        backtrack(stop)

for tc in range(1, T+1):
    bus = list(map(int, input().split()))
    N, BS = bus[0], bus[1:]
    cnt = now = 0
    backtrack(now)
    print('#{} {}'.format(tc, cnt))