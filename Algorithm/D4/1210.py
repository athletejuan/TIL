for _ in range(1, 11):
    T = input()
    dx = [1, -1]
    ladder = []
    q = []
    for _ in range(100):
        ladder.append(list(map(int, input().split())))
    for i in range(100):
        if ladder[99][i] == 2:
            q.append((99,i))
            break
    while q:
        y,x = q.pop()
        if not y:
            print(f'#{T} {x}')
            break
        for j in range(2):
            nx = x+dx[j]
            if 0 <= nx < 100:
                if ladder[y][nx]:
                    q.append((y, nx))
                    ladder[y][x] = 0
                    break
        else:
            q.append((y-1, x))