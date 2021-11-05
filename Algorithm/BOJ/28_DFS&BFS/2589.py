def BFS(r,c):
    global longest
    stack = [[r,c]]
    visited = [[0]*C for _ in range(R)]
    visited[r][c] = 1
    dist = 0
    while True:
        temp = []
        while stack:
            r,c = stack.pop()
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < R and 0 <= nc < C and maps[nr][nc] == 'L' and not visited[nr][nc]:
                    temp.append([nr, nc])
                    visited[nr][nc] = 1
        if temp:
            stack = temp
            dist += 1
        else:
            break
    if longest < dist:
        longest = dist


R,C = map(int, input().split())
maps = [list(input()) for _ in range(R)]
dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
longest = 0

for i in range(R):
    for j in range(C):
        if maps[i][j] == 'L':
            BFS(i,j)
print(longest)