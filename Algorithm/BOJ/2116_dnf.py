N = int(input())

ct = []
answer = []

for _ in range(N):
    ct.append(list(map(int, input().split())))
for i in range(6):
    j = 0
    six = []
    nxt = ct[0][i]
    six.append(nxt)
    while j < N:
        if ct[j].index(nxt) == 0:
            nxt = ct[j][5]
        elif ct[j].index(nxt) == 1:
            nxt = ct[j][3]
        elif ct[j].index(nxt) == 2:
            nxt = ct[j][4]
        elif ct[j].index(nxt) == 3:
            nxt = ct[j][1]
        elif ct[j].index(nxt) == 4:
            nxt = ct[j][2]
        else:
            nxt = ct[j][0]
        six.append(nxt)
        j += 1
    cnt = 0
    for idx, value in enumerate(six):
        if value == 6:
            if not idx:
                cnt += 1
                if six[1] == 5:
                    cnt += 1
            elif idx == N:
                cnt += 1
                if six[N-2] == 5:
                    cnt += 1
            else:
                cnt += 2
                if six[idx-1] == 5 or six[idx+1] == 5:
                    cnt += 1
    answer.append(6*N - cnt)
print(max(answer))