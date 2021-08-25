T = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def BFS():
    while move:
        x, y = move.pop(0)
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a < N and 0 <= b < N and not dist[a][b]:
                if maze[a][b] == '0':
                    move.append([a, b])
                    dist[a][b] = dist[x][y] + 1
                elif maze[a][b] == '3':
                    return dist[x][y]
    return 0

for tc in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    move = []
    dist = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                move.append([i,j])
                break
    print('#{} {}'.format(tc, BFS()))


# live code
# def search():
#     for i in range(N):
#         for j in range(N):
#             if maze[i][j] == '2':
#                 return i,j

# def BFS(S,G):
#     # 선형큐 활용
#     Q = [0] * 1000000
#     front, rear = -1, 0
#     Q[rear] = (S,G)

#     dist = [[-1] * N for _ in range(N)]
#     dist[S][G] = 0

#     # 선형큐에서 공백 검사
#     while front != rear:
#         front += 1
#         curr_r, curr_c = Q[front]
#         if maze[curr_r][curr_c] == '3':
#             return dist[curr_r][curr_c] - 1
#         for i in range(4):
#             nr = curr_r + dx[i]
#             nc = curr_c + dy[i]

#             # 벽으로 둘러싸지 않았기 때문에 범위검사를 해야함
#             if nr < 0 or nr >= N or nc < 0 or nc >= N:
#                 continue
#             # 벽이 아니면서, 거리를 갱신하지 않았다면 좌표를 넣고 갱신
#             if maze[nr][nc] != '1' and dist[nr][nc] == -1:
#                 dist[nr][nc] = dist[curr_r][curr_c] + 1
#                 rear += 1
#                 Q[rear] = (nr, nc)
#     return 0


# for tc in range(1, T+1):
#     N = int(input())
#     maze = [list(input()) for _ in range(N)]

#     S,G = search()
#     print('#{} {}'.format(tc, BFS(S,G)))


# 1st try
# T = int(input())
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
#
# def BFS():
#     global move
#     while way:
#         R = len(way)
#         move += 1
#         for _ in range(R):
#             x, y = way.pop(0)
#             for i in range(4):
#                 a = x + dx[i]
#                 b = y + dy[i]
#                 maze[x][y] = '1'
#                 if 0 <= a < N and 0 <= b < N:
#                     if maze[a][b] == '0':
#                         way.append([a, b])
#                     elif maze[a][b] == '2':
#                         move -= 1
#                         return
#             if not way:
#                 move = 0
#                 return
#
# for tc in range(1, T+1):
#     N = int(input())
#     maze = [list(input()) for _ in range(N)]
#     way = []
#     move = 0
#
#     for i in range(N):
#         for j in range(N):
#             if maze[i][j] == '3':
#                 way.append([i,j])
#                 break
#     BFS()
#     print('#{} {}'.format(tc, move))