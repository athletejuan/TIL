T = int(input())

for tc in range(T):
    N = int(input())
    players = [int(input())-1 for _ in range(N)]
    target = [players[0]]
    K = 1
    for i in range(N-1):
        now = target[-1]
        if now == N-1:
            break
        target.append(players[now])
        K += 1
    else:
        K = 0
    print(K)
