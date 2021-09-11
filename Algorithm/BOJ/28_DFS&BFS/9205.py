t = int(input())

for _ in range(t):
    n = int(input())
    hx, hy = map(int, input().split())
    cs = [list(map(int, input().split())) for _ in range(n)]
    gx, gy = map(int, input().split())

    stack = [[hx, hy]]
    visited = [0]*n
    while stack:
        hx, hy = stack.pop()
        fx = gx - hx if gx > hx else hx - gx
        fy = gy - hy if gy > hy else hy - gy
        if fx + fy < 1001:
            print('happy')
            break
        for i in range(n):
            if not visited[i]:
                dx = cs[i][0] - hx if cs[i][0] > hx else hx - cs[i][0]
                dy = cs[i][1] - hy if cs[i][1] > hy else hy - cs[i][1]
                if dx + dy < 1001:
                    stack.append(cs[i])
                    visited[i] = 1
    else:
        print('sad')