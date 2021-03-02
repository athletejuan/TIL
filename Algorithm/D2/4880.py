T = int(input())

def winner(x,y):
    if (tournament[x-1] - tournament[y-1])%3 < 2:
        return x
    return y

def vs(start, end):
    if start == end:
        return start

    fore, back = vs(start, (start+end)//2), vs((start+end)//2+1, end)
    return winner(fore, back)

for tc in range(1, T+1):
    N = int(input())
    tournament = list(map(int, input().split()))
    start = 1
    end = N
    print('#{} {}'.format(tc, vs(start, end)))
    # mid = (start + end) // 2
    # while mid > 1:
    #     fore, back = tournament[:mid], tournament[mid:]
    #     vs(fore)
    #     vs(back)
    #     mid = len(fore)//2
