T = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def BFS():
    global move
    while way:
        R = len(way)
        move += 1
        for _ in range(R):
            x, y = way.pop(0)
            for i in range(4):
                a = x + dx[i]
                b = y + dy[i]
                maze[x][y] = '1'
                if 0 <= a < N and 0 <= b < N:
                    if maze[a][b] == '0':
                        way.append([a, b])
                    elif maze[a][b] == '2':
                        move -= 1
                        return
            if not way:
                move = 0
                return

for tc in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    way = []
    move = 0

    for i in range(N):
        for j in range(N):
            if maze[i][j] == '3':
                way.append([i,j])
                break
    BFS()
    print('#{} {}'.format(tc, move))