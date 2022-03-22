T = int(input())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x,y,n):
    if len(n) > 6:
        numbers.add(n)
        return
    for i in range(4):
        a,b = x+dx[i],y+dy[i]
        if 0 <= a < 4 and 0 <= b < 4:
            DFS(a,b,n+base[a][b])

for tc in range(1, T+1):
    base = [input().split() for _ in range(4)]
    numbers = set()

    for i in range(4):
        for j in range(4):
            DFS(i,j,base[i][j])
    print('#{} {}'.format(tc, len(numbers)))