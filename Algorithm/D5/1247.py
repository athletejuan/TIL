def navigate(S, arr, G):
    global shortest
    route = 0
    for j in range(N):
        route += abs(S[0] - C[arr[j]][0]) + abs(S[1] - C[arr[j]][1])
        S = C[arr[j]]
    route += abs(S[0] - G[0]) + abs(S[1] - G[1])
    if shortest > route:
        shortest = route


def combination(used, now, cnt):
    if cnt == N:
        navigate(O, comb, H)
    for i in range(N):
        if not used[i]:
            now.append(arr[i])
            used[i] = 1
            combination(used, now, cnt+1)
            now.pop()
            used[i] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    position = list(map(int, input().split()))
    spot = []
    for i in range(N+2):
        spot.append([position[i*2], position[i*2+1]])
    O,H,C = spot[0], spot[1], spot[2:]
    arr = [i for i in range(N)]
    used, comb = [0] * N, []
    shortest, cnt = 100*N, 0
    combination(used, comb, cnt)
    print('#{} {}'.format(tc, shortest))