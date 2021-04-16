T = int(input())

def DFS(i):
    global group
    group += 1
    stack = [i]
    while stack:
        i = stack.pop()
        for k in range(1, N+1):
            if base[i][k]:
                stack.append(k)
                base[i][k] = base[k][i] = 0

for tc in range(1, T+1):
    N,M = map(int, input().split())
    base = [[0]*(N+1) for _ in range(N+1)]
    submit = list(map(int, input().split()))
    for num in submit:
        base[0][num] = 1
    pair = [[submit[2*i], submit[2*i+1]] for i in range(M)]
    for p in pair:
        base[p[0]][p[1]] = base[p[1]][p[0]] = 1
    group = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if base[i][j]:
                DFS(i)
    print('#{} {}'.format(tc, N-sum(base[0])+group))