def escape(q):
    for r,c in q:
        if r == x and c == y:
            return True


def water():
    global w
    temp = []
    while w:
        r,c = w.pop()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < R and 0 <= nc < C and forest[nr][nc] != 'D' and forest[nr][nc] != 'X' and visited[nr][nc] < 1:
                forest[nr][nc] = '*'
                visited[nr][nc] = 1
                temp.append([nr, nc])
    w = temp


def beaver():
    global b
    temp = []
    while b:
        r,c = b.pop()
        if forest[r][c] != '*':
            forest[r][c] = '*'
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                    if forest[nr][nc] == '.' or forest[nr][nc] == 'D':
                        temp.append([nr, nc])
                        visited[nr][nc] = -1
    if temp:
        b = temp
        return True


R,C = map(int, input().split())
forest = [list(input()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
b, w, m = [], [], 0
for i in range(R):
    for j in range(C):
        if forest[i][j] == '*':
            w.append([i,j])
        if forest[i][j] == 'S':
            b.append([i,j])
        if forest[i][j] == 'D':
            x,y = i,j

while not escape(b):
    if not beaver():
        print('KAKTUS')
        break
    water()
    m += 1
else:
    print(m)