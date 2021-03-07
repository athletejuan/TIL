dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x,y):
    queue = [[x,y]]
    while queue:
        x,y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 100 and 0 <= ny < 100:
                if maze[nx][ny] == '0':
                    queue.append([nx,ny])
                    maze[nx][ny] = '1'
                elif maze[nx][ny] == '3':
                    return 1
    return 0

for i in range(10):
    tc = input()
    maze = [list(input()) for _ in range(100)]
    for i in range(100):
        for j in range(100):
            if maze[i][j] == '2':
                x,y = i,j
                break
    print('#{} {}'.format(tc, BFS(x,y)))


# 1st try
# for _ in range(1, 11):
#     T = input()
#     maze = [list(map(int, list(input()))) for _ in range(100)]
#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]
#     q = []
#     breaker = False
#     for i in range(100):
#         for j in range(100):
#             if maze[i][j] == 2:
#                 q.append((i,j))
#                 breaker = True
#                 break
#         if breaker:
#             break
#
#     while q:
#         x,y = q.pop()
#         if maze[x][y] == 3:
#             print(f'#{T} 1')
#             break
#         for k in range(4):
#             nx,ny = x+dx[k],y+dy[k]
#             if 0<=nx<99 and 0<=ny<99:
#                 if not maze[nx][ny] or maze[nx][ny] == 3:
#                     q.append((nx,ny))
#                     maze[x][y] = 1
#     else:
#         print(f'#{T} 0')