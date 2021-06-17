import sys
input = sys.stdin.readline

N,M,B = map(int, input().split())
mine = []
mini, maxi, total, final = 256, 0, 0, 0

def craft(height):
    global total, final
    need, time = 0, 0
    for i in range(N):
        for j in range(M):
            need += height - mine[i][j]
            if height > mine[i][j]:
                time += (height - mine[i][j])
            elif height < mine[i][j]:
                time += 2*(mine[i][j] - height)
    if need > B:
        return
    if not total or time < total:
        final = height
    return time

for _ in range(N):
    row = list(map(int, input().split()))
    for i in range(M):
        if mini > row[i]:
            mini = row[i]
        if maxi < row[i]:
            maxi = row[i]
    mine.append(row)

if maxi == mini:
    print(0, maxi)
else:
    while maxi >= mini:
        time = craft(maxi)
        if total and time and time > total:
            break
        else:
            total = time
        maxi -= 1
    print(total, final)