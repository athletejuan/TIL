T = int(input())

def runway(field, i):
    global cnt
    way = []
    for j in range(N):
        if not way:
            way.append(field[i][j])
        else:
            if field[i][j] < way[-1]-1 or way[-1]+1 < field[i][j]:
                return
            if way[-1] == field[i][j]:
                way.append(field[i][j])
            elif way[-1] + 1 == field[i][j]:
                if len(way) < X:
                    return
                else:
                    for k in range(X):
                        if len(way) > X + k and way[-1-(X+k)] > way[-1]:
                            return
                        if way[-1-k] != field[i][j] - 1:
                            return
                    way.append(field[i][j])
            elif way[-1] - 1 == field[i][j]:
                if len(way) > X-1:
                    for l in range(X):
                        if field[i][j]+1 < way[-1-l]:
                            return
                else:
                    for k in range(j):
                        if way[k] > field[i][j] + 1:
                            return
                way.append(field[i][j])
    else:
        for m in range(1, X):
            if way[-1] < way[-1-m]:
                return
        else:
            cnt += 1

for tc in range(1, T+1):
    N,X = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(N)]
    col_field = list(map(list, zip(*field)))
    cnt = 0

    for i in range(N):
        runway(field, i)
        runway(col_field, i)

    print('#{} {}'.format(tc, cnt))