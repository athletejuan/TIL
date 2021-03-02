T = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DFS():
    while way:
        now = way.pop()
        x,y = now[0], now[1]
        maze[x][y] = '1'
        for i in range(4):
            a,b = x + dx[i], y + dy[i]
            if 0 <= a < N and 0 <= b < N:
                if maze[a][b] == '0':
                    way.append([a,b])
                elif maze[a][b] == '3':
                    return 1
    return 0

for tc in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    way = []
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                way.append([i,j])
    print('#{} {}'.format(tc, DFS()))


# 1st try
# for test_case in range(1, T+1):
#     N = int(input())
#     matrix = [list(map(int, list(input()))) for _ in range(N)]
#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]
#     q = []
#     breaker = False
#     result = False
#
#     for i in range(N):
#         for j in range(N):
#             if matrix[i][j] == 2:
#                 start = (i,j)
#                 breaker = True
#                 break
#         if breaker:
#             break
#     q.append(start)
#
#     while q:
#         y,x = q.pop()
#         for k in range(4):
#             nx,ny = x+dx[k],y+dy[k]
#             if 0 <= nx < N and 0 <= ny < N:
#                 if not matrix[ny][nx]:
#                     matrix[y][x] = 1
#                     q.append((ny,nx))
#                 elif matrix[ny][nx] == 3:
#                     result = True
#                     break
#     if result:
#         print(f'#{test_case} 1')
#     else:
#         print(f'#{test_case} 0')