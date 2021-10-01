T = int(input())

for tc in range(1, T+1):
    N,E = input().split()
    N,E,L = list(N), int(E), len(N)
    now, big = 0, '0'

    while E and big == '0':
        for i in range(now, L):
            if N[now] < N[i]:
                if big < N[i]:
                    big = N[i]
                    bigs = [i]
                elif big == N[i]:
                    bigs.append(i)
        if big != '0':
            if E < len(bigs):
                N[now], N[bigs[-E]] = N[bigs[-E]], N[now]
            else:
                N[now], N[bigs[0]] = N[bigs[0]], N[now]
            big = '0'
            E -= 1
        now += 1
        if now > L:
            break
    if len(N) == len(set(N)) and E%2:
        N[-1], N[-2] = N[-2], N[-1]
    print('#{} {}'.format(tc, ''.join(N)))