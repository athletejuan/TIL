T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, list(input()))) for _ in range(N)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = []
    breaker = False
    result = False

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                start = (i,j)
                breaker = True
                break
        if breaker:
            break
    q.append(start)

    while q:
        y,x = q.pop()
        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            if 0 <= nx < N and 0 <= ny < N: 
                if not matrix[ny][nx]:
                    matrix[y][x] = 1
                    q.append((ny,nx))
                elif matrix[ny][nx] == 3:
                    result = True
                    break
    if result:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')
