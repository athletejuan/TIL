from collections import deque

M,N = map(int, input().split())
box = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for _ in range(N):
    box.append(list(map(int, input().split())))

tomatoes = deque()
for x in range(N):
    for y in range(M):
        if box[x][y] == 1:
            tomatoes.append([x,y])

while tomatoes:
    a,b = tomatoes.popleft()
    for i in range(4):
        x = a+dx[i]
        y = b+dy[i]
        if 0 <= x < N and 0 <= y < M and not box[x][y]:
            tomatoes.append([x, y])
            box[x][y] = box[a][b] + 1

for row in box:
    if 0 in row:
        print(-1)
        break
else:
    print(box[a][b]-1)


# 메모리 초과
# M,N = map(int, input().split())
# box = []
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
# day = -1
# for _ in range(N):
#     box.append(list(map(int, input().split())))

# def BFS(x,y):
#     box[x][y] = 1
#     for i in range(4):
#         if 0 <= x+dx[i] < N and 0 <= y+dy[i] < M and not box[x+dx[i]][y+dy[i]]:
#             next_tmt.append([x+dx[i], y+dy[i]])

# start = []
# for x in range(N):
#     for y in range(M):
#         if box[x][y] == 1:
#             start.append([x,y])

# while start:
#     next_tmt = []
#     for tomato in start:
#         BFS(tomato[0], tomato[1])
#     start = next_tmt
#     day += 1

# for row in box:
#     if 0 in row:
#         print(-1)
#         break
# else:
#     print(day)