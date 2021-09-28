N = int(input())
K = int(input())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
dir = time = rotate = 0
flag = True
snake = [[0, 0]]
field = [[0]*N for _ in range(N)]

for _ in range(K):
    r,c = map(int, input().split())
    field[r-1][c-1] = 1
L = int(input())
dirs = [list(input().split()) for _ in range(L)]
r = c = 0

while flag:
    if rotate < L and time == int(dirs[rotate][0]):
        if dirs[rotate][1] == 'D':
            dir += 1
        else:
            dir -= 1
        rotate += 1
    nr, nc = r + dr[dir%4], c + dc[dir%4]
    if 0 <= nr < N and 0 <= nc < N and [nr, nc] not in snake:
        snake.append([nr, nc])
        if field[nr][nc]:
            field[nr][nc] = 0
        else:
            snake.pop(0)
        time += 1
        r, c = nr, nc
    else:
        flag = False

print(time+1)