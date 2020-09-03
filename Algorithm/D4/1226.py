for _ in range(1, 11):
    T = input()
    maze = [list(map(int, list(input()))) for _ in range(16)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = []
    breaker = False
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                q.append((i,j))
                breaker = True
                break
        if breaker:
            break

    while q:
        x,y = q.pop()
        if maze[x][y] == 3:
            print(f'#{T} 1')
            break
        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            if 0<=nx<15 and 0<=ny<15:
                if not maze[nx][ny] or maze[nx][ny] == 3:
                    q.append((nx,ny))
                    maze[x][y] = 1
    else:
        print(f'#{T} 0')