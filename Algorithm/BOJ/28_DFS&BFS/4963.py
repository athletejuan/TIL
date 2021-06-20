dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

def BFS(x,y):
    world[x][y] = 0
    land = [[x,y]]
    while land:
        x,y = land[0][0], land[0][1]
        del land[0]
        for k in range(8):
            if 0 <= x+dx[k] < h and 0 <= y+dy[k] < w and world[x+dx[k]][y+dy[k]]:
                world[x+dx[k]][y+dy[k]] = 0
                land.append([x+dx[k],y+dy[k]])

while True:
    w,h = map(int, input().split())
    if not w and not w:
        break
    world = []

    for _ in range(h):
        world.append(list(map(int, input().split())))

    island = 0
    for i in range(h):
        for j in range(w):
            if world[i][j]:
                island += 1
                BFS(i,j)
                # land = [[i,j]]
                # while land:
                #     x,y = land[0][0], land[0][1]
                #     del land[0]
                #     world[x][y] = 0
                #     for k in range(8):
                #         if 0 <= x+dx[k] < h and 0 <= y+dy[k] < w and world[x+dx[k]][y+dy[k]]:
                #             world[x+dx[k]][y+dy[k]] = 0
                #             land.append([x+dx[k],y+dy[k]])
    print(island)