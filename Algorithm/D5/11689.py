T = int(input())
move = []

for tc in range(1, T+1):
    a,b = map(int, input().split())
    cnt = 0
    while a > 1 and b > 1:
        if a > b:
            cnt += a//b
            a = a%b
        else:
            cnt += b//a
            b = b%a
    if a < b:
        a,b = b,a
    cnt += a-1
    move.append(cnt)

for tc in range(len(move)):
    print('#{} {}'.format(tc+1, move[tc]))