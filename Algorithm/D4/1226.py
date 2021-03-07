dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x,y):
    global flag
    if maze[x][y] == '3':
        flag = 1
        return
    maze[x][y] = '1'
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 16 and 0 <= ny < 16:
            if maze[nx][ny] != '1':
                DFS(nx,ny)

for i in range(10):
    tc = input()
    maze = [list(input()) for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if maze[i][j] == '2':
                x,y = i,j
                break
    flag = 0
    DFS(x,y)
    print('#{} {}'.format(tc, flag))


# 1st try
# for _ in range(1, 11):
#     T = input()
#     maze = [list(map(int, list(input()))) for _ in range(16)]
#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]
#     q = []
#     breaker = False
#     for i in range(16):
#         for j in range(16):
#             if maze[i][j] == 2:
#                 q.append((i,j))
#                 breaker = True
#                 break
#         if breaker:
#             break

#     while q:
#         x,y = q.pop()
#         if maze[x][y] == 3:
#             print(f'#{T} 1')
#             break
#         for k in range(4):
#             nx,ny = x+dx[k],y+dy[k]
#             if 0<=nx<15 and 0<=ny<15:
#                 if not maze[nx][ny] or maze[nx][ny] == 3:
#                     q.append((nx,ny))
#                     maze[x][y] = 1
#     else:
#         print(f'#{T} 0')


# live code
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]

# def BFS(r,c):
#     Q = [(r, c)]

#     while Q:
#         cur_r, cur_c = Q.pop(0)
#         # 서있는 위치가 도착지점인지 확인
#         for i in range(4):
#             nr = cur_r+dr[i]
#             nc = cur_c+dc[i]

#             if nr < 0 or nr >= N or nc < 0 or nc >= N:
#                 continue
#             if maze[nr][nc] == 3:
#                 return 1
#             if maze[nr][nc] != 1:
#                 Q.append((nr, nc))
#                 maze[nr][nc] = 1
#     return 0

# def DFS(r,c):
#     global flag
#     if maze[r][c] == 3:
#         flag = 1
#         return
#     maze[r][c] = 1

#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]

#     if nr < 0 or nr >= N or nc < 0 or nc >= N:
#         continue
#     if maze[nr][nc] != 1:
#         DFS(nr, nc)

# for _ in range(10):
#     tc = input()
#     N = 16

#     maze = [list(map(int, input())) for _ in range(N)]

#     for i in range(N):
#         for j in range(N):
#             if maze[i][j] == 2:
#                 sR, sC = i, j
#                 maze[i][j] = 1
#     # BFS
#     # print('#{} {}'.format(tc, BFS(sR, sC)))
#     # DFS
#     flag = 0
#     DFS(sR, sC)
#     print('#{} {}'.format(tc, flag))