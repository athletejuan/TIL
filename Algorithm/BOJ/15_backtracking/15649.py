N,M = map(int, input().split())
picked = []

def array(N,M):
    if M == 0:
        return print(' '.join(picked))
    for _ in range(1, N+1):
        if not picked or str(_) not in picked:
            picked.append(str(_))
            array(N, M-1)
            picked.pop()

array(N,M)