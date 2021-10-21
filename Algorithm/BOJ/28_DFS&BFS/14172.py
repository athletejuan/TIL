N = int(input())
cows = [list(map(int, input().split())) for _ in range(N)]
moo = 0


def DFS(cow):
    global moo
    check, cnt = [0]*N, 0
    cast = [cow]
    while cast:
        x,y,p = cast.pop()
        for j in range(N):
            if not check[j] and (x-cows[j][0])**2+(y-cows[j][1])**2 <= p**2:
                cnt += 1
                check[j] = 1
                cast.append(cows[j])
    if moo < cnt:
        moo = cnt


for i in range(N):
    DFS(cows[i])
print(moo)