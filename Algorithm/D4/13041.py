T = int(input())

for tc in range(1, T+1):
    N,K = map(int, input().split())
    pick = list(map(int, input().split()))
    waste = list(map(int, input().split()))
    check = [0] * (K+1)
    decision, wait, required = set(), [], 0

    for i in range(N):
        decision.add(pick[i])
        if len(decision) == K:
            print('#{} {}'.format(tc, 0))
            break
        if check[pick[i]] < waste[i]:
            if check[pick[i]]:
                wait.append(check[pick[i]])
            check[pick[i]] = waste[i]
        else:
            wait.append(waste[i])
    else:
        wait.sort()
        K -= len(decision)
        for j in range(K):
            required += wait[j]
        print('#{} {}'.format(tc, required))