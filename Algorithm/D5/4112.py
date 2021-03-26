T = int(input())

def pyramid(x,y):
    room = plus = row = 1
    start = 0
    while room < x:
        if room >= y and not start:
            start = [row, y-(room-plus)]
        plus += 1
        room += plus
        row += 1
    end = [row, x-(room-plus)]
    if not start:
        return x-y
    else:
        if end[1] > start[1]:
            return max(end[0]-start[0], end[1]-start[1])
        else:
            return max(end[0]-start[0], end[0]-start[0]-end[1]+start[1])

for tc in range(1, T+1):
    a,b = map(int, input().split())
    if a < b:
        a,b = b,a
    print('#{} {}'.format(tc,pyramid(a,b)))