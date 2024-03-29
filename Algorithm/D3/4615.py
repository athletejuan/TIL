T = int(input())
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def othello(this):
    # 다른 색의 돌이 있는 방향으로 다른 색의 돌을 찾아감(i가 방향)
    x, y, i = this[-1][0] + dx[this[-1][2]], this[-1][1] + dy[this[-1][2]], this[-1][2]
    if 0 <= x < N and 0 <= y < N:
        # 비어있지 않고 다른 색의 돌을 찾은 경우 this list에 누적하고 해당 좌표로 다시 othello함수 실행
        if board[x][y] and board[x][y] != c:
            this.append([x, y, i])
            othello(this)
        # 같은 색의 돌을 만난 경우에만 this list에 담긴 좌표의 돌들을 같은 색으로 교환
        elif board[x][y] == c:
            for ex in this:
                board[ex[0]][ex[1]] = c

for tc in range(1, T+1):
    N,M = map(int, input().split())
    B,W = 0,0
    emp = N//2-1
    # 오셀로 보드 초기화
    board = [[0]*N for _ in range(emp)]
    board += [[0]*emp+[2-i]+[i+1]+[0]*emp for i in range(2)]
    board += [[0]*N for _ in range(emp)]

    for _ in range(M):
        x,y,c = map(int, input().split())
        x,y = x-1, y-1
        board[x][y] = c
        ready = []
        # 새로운 돌을 놓은 자리 주변 8자리에 다른 색의 돌이 있는지 확
        for i in range(8):
            a = x+dx[i]
            b = y+dy[i]
            if 0 <= a < N and 0 <= b < N and board[a][b] and board[a][b] != c:
                ready.append([a,b,i])
        # 다른 색의 돌이 있는 방향을 모두 확인
        while ready:
            this = [ready.pop()]
            othello(this)

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                B += 1
            elif board[i][j] == 2:
                W += 1
    print('#{} {} {}'.format(tc, B, W))


# 1st try
# T = int(input())
# dx = [-1, -1, 0, 1, 1, 1, 0, -1]
# dy = [0, 1, 1, 1, 0, -1, -1, -1]

# for tc in range(1, T+1):
#     N,M = map(int, input().split())
#     emp = N//2-1
#     board = [[0]*N for _ in range(emp)]
#     board += [[0]*emp+[2-i]+[i+1]+[0]*emp for i in range(2)]
#     board += [[0]*N for _ in range(emp)]

#     for _ in range(M):
#         x,y,c = map(int, input().split())
#         x,y = x-1, y-1
#         board[x][y] = c
#         ready = []
#         for i in range(8):
#             a = x+dx[i]
#             b = y+dy[i]
#             if 0 <= a < N and 0 <= b < N and board[a][b] and board[a][b] != c:
#                 ready.append([a,b,i])
#         while ready:
#             this = []
#             now = ready.pop()
#             this.append(now)
#             while True:
#                 x,y,i = this[-1][0]+dx[this[-1][2]], this[-1][1]+dy[this[-1][2]], this[-1][2]
#                 if 0 <= x < N and 0 <= y < N:
#                     if board[x][y] and board[x][y] != c:
#                         this.append([x,y,i])
#                     elif board[x][y] == c:
#                         for ch in this:
#                             board[ch[0]][ch[1]] = c
#                         break
#                     else:
#                         break
#                 else:
#                     break

#     B, W = 0, 0
#     for i in range(N):
#         for j in range(N):
#             if board[i][j] == 1:
#                 B += 1
#             elif board[i][j] == 2:
#                 W += 1
#     print('#{} {} {}'.format(tc, B, W))