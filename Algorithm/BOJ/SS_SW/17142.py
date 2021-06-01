N,M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
viruses, time, zeros = [], -1, 0
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def check(cnt):
    global time
    for i in range(N):
        for j in range(N):
            if not lab[i][j]:
                return
    else:
        time = cnt

def bfs(order):
    global time, zeros
    cnt = 0
    starts, temp = [], []
    for i in order:
        starts.append(viruses[i])
    while zeros:
        while starts:
            for j in range(len(starts)):
                x,y = starts.pop()
                for k in range(4):
                    a,b = x+dx[k], y+dy[k]
                    if 0 <= a < N and 0 <= b < N:
                        if not lab[a][b]:
                            lab[a][b] += 3
                            temp.append([a,b])
                            zeros -= 1
                        elif lab[a][b] == 2:
                            lab[a][b] += 3
                            temp.append([a,b])
        cnt += 1
        if not zeros or not temp:
            break
        else:
            starts = temp
            temp = []

    if time < 0 or cnt < time:
        check(cnt)
    for i in range(N):
        for j in range(N):
            if lab[i][j] > 2:
                lab[i][j] -= 3
                if not lab[i][j]:
                    zeros += 1

def pick(n, picked, toPick):
    if toPick == 0:
        bfs(picked)

    smallest = 0 if not picked else picked[-1]
    for i in range(smallest, n):
        if i not in picked:
            picked.append(i)
            pick(n, picked, toPick - 1)
            picked.pop()

for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            viruses.append([i,j])
        elif not lab[i][j]:
            zeros += 1

pick(len(viruses), [], M)
print(time)