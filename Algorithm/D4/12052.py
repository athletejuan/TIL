T = int(input())

def check():
    global possible
    for i in range(N):
        for j in range(M):
            if floor[i][j] == '#':
                if i < N-1 and j < M-1 and floor[i+1][j] == '#' and floor[i][j+1] == '#' and floor[i+1][j+1] == '#':
                    floor[i+1][j] = floor[i][j+1] = floor[i+1][j+1] = '.'
                else:
                    possible = 'NO'
                    return

for tc in range(1, T+1):
    N,M = map(int, input().split())
    floor = [list(input()) for _ in range(N)]
    possible = 'YES'
    check()

    print('#{} {}'.format(tc, possible))