T = int(input())

def dock():
    global fin, cnt
    temp = 25
    for i in range(N):
        if trucks[i][0] >= fin and temp >= trucks[i][1]:
            temp = trucks[i][1]
    fin = temp
    cnt += 1

for tc in range(1, T+1):
    N = int(input())
    trucks = [list(map(int, input().split())) for i in range(N)]
    fin, last = 25, 0
    cnt = 1

    for i in range(N):
        if fin > trucks[i][1]:
            fin = trucks[i][1]
        if last < trucks[i][0]:
            last = trucks[i][0]

    while fin <= last:
        dock()
    print('#{} {}'.format(tc, cnt))