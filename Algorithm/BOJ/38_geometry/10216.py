def BFS(idx, enemy):
    groups = [enemy]
    while groups:
        x,y,R = groups.pop()
        for i in range(idx+1, N):
            if not check[i] and (enemies[i][0]-x)**2 + (enemies[i][1]-y)**2 <= (R+enemies[i][2])**2:
                check[i] = 1
                groups.append(enemies[i])


T = int(input())
for _ in range(T):
    N = int(input())
    enemies = [list(map(int, input().split())) for _ in range(N)]
    check, group = [0] * N, 0

    for i in range(N):
        if not check[i]:
            group += 1
            BFS(i, enemies[i])
    print(group)