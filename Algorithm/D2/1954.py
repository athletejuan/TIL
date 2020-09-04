T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    snail = [[0]*N for i in range(N)]
    snail[0][0] = 1
    d = [1, 1, -1, -1]
    q = [(0,0)]
    v = 0
    
    while q:
        y,x = q.pop()
        if not v%2:
            nx = x+d[v%4]
            if 0<= nx < N and not snail[y][nx]:
                q.append((y,nx))
                snail[y][nx] = snail[y][x] + 1
            else:
                v += 1
                if snail[y][x] != N**2:
                    q.append((y,x))
        else:
            ny = y+d[v%4]
            if 0 <= ny < N and not snail[ny][x]:
                q.append((ny,x))
                snail[ny][x] = snail[y][x] + 1
            else:
                v += 1
                q.append((y,x))

    print(f'#{test_case}')
    for _ in range(N):
        print(' '.join(map(str, snail[_])))