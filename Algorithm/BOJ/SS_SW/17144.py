R,C,T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
total = 0
dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

def diffuse(dusts):
    dirt = [[0] * C for _ in range(R)]
    while dusts:
        r,c = dusts.pop()
        dust = room[r][c]
        for i in range(4):
            a,b = r+dr[i], c+dc[i]
            if 0 <= a < R and 0 <= b < C:
                if room[a][b] != -1:
                    dirt[a][b] += dust//5
                    room[r][c] -= dust//5
    for i in range(R):
        for j in range(C):
            room[i][j] += dirt[i][j]

def purify(top, bottom):
    for i in range(top[0]-2, -1, -1):
        room[i+1][0] = room[i][0]
    for j in range(1, C):
        room[0][j-1] = room[0][j]
    for k in range(top[0]):
        room[k][C-1] = room[k+1][C-1]
    for l in range(C-1, 1, -1):
        room[top[0]][l] = room[top[0]][l-1]
    for i in range(bottom[0]+1, R-1):
        room[i][0] = room[i+1][0]
    for j in range(C-1):
        room[R-1][j] = room[R-1][j+1]
    for k in range(R-1, bottom[0], -1):
        room[k][C-1] = room[k-1][C-1]
    for l in range(C-1, 1, -1):
        room[bottom[0]][l] = room[bottom[0]][l-1]
    room[top[0]][1], room[bottom[0]][1] = 0, 0

for _ in range(T):
    dusts, purifier = [], []
    for i in range(R):
        for j in range(C):
            if room[i][j] > 4:
                dusts.append([i,j])
            if room[i][j] < 0:
                purifier.append([i,j])
    diffuse(dusts)
    purify(purifier[0], purifier[1])

for i in range(R):
    for j in range(C):
        total += room[i][j]
print(total+2)