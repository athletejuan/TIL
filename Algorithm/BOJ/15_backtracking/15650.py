N,M = map(int, input().split())

def select(N, picked, M):
    if not M:
        return print(' '.join(picked))
    mini = 0 if not picked else int(picked[-1])
    for i in range(mini, N):
        picked.append(str(i+1))
        select(N, picked, M-1)
        picked.pop()

select(N, [], M)