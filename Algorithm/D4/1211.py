for _ in range(1, 11):
    T = input()
    dx = [1, -1]
    ladder = []
    visited = [[0]*100 for _ in range(100)]
    checked = [[0]*100 for _ in range(100)]
    q = []
    for _ in range(100):
        ladder.append(list(map(int, input().split())))
    for i in range(100):
        if ladder[0][i]:
            q.append((0,i))
    dis = {}
    while q:
        y,x = q.pop()
        if not y:
            s = x
        elif y == 99:
            dis[visited[99][x]] = s
            checked = [[0]*100 for _ in range(100)]
            continue
        for j in range(2):
            nx = x+dx[j]
            if 0 <= nx < 100:
                if ladder[y][nx] and not checked[y][nx]:
                    q.append((y, nx))
                    checked[y][x] = 1
                    visited[y][nx] = visited[y][x] + 1
                    print('side', visited[y][nx])
                    break
        else:
            q.append((y+1, x))
            visited[y+1][x] = visited[y][x] + 1
            print('down', y+1, visited[y+1][x])

    print(f'#{T} {dis[min(dis.keys())]}')