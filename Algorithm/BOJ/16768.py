N,K = map(int, input().split())
MY = [list(input()) for _ in range(N)]
flag = True

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def connect(x,y,c):
    stack, temp = [[x,y]], [[x,y]]
    check = 1
    while stack:
        x,y = stack.pop()
        visited[x][y] = 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < 10 and MY[nx][ny] == c and not visited[nx][ny]:
                stack.append([nx, ny])
                temp.append([nx, ny])
                visited[nx][ny] = 1
                check += 1
    if check >= K:
        for r,c in temp:
            MY[r][c] = 0

def gravity():
    global flag
    flag = False
    for k in range(10):
        stack, blank = [], []
        for l in range(N-1, -1, -1):
            if MY[l][k] == '0' or not MY[l][k]:
                blank.append('0')
                if not MY[l][k]:
                    flag = True
            else:
                stack.append(MY[l][k])
        column = stack + blank
        for m in range(N):
            MY[N-m-1][k] = column[m]

while flag:
    visited = [[0] * 10 for _ in range(N)]
    for i in range(N):
        for j in range(10):
            if MY[i][j] != '0' and not visited[i][j]:
                connect(i,j,MY[i][j])
    gravity()

for i in range(N):
    print(''.join(MY[i]))