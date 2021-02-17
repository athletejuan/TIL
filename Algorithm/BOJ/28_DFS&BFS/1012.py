T = int(input())

for t in range(T):
    M, N, K = map(int, input().split())
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    c = []
    b = 0
    for _ in range(K):
        c.append(list(map(int, input().split())))
    while c:
        b += 1
        s = c.pop()
        l = []
        for i in range(4):
            if [s[0]+dx[i], s[1]+dy[i]] in c:
                l.append([s[0]+dx[i], s[1]+dy[i]])
                c.remove([s[0]+dx[i], s[1]+dy[i]])
        while l:
            m = l.pop()
            for j in range(4):
                if [m[0]+dx[j], m[1]+dy[j]] in c:
                    l.append([m[0]+dx[j], m[1]+dy[j]])
                    c.remove([m[0]+dx[j], m[1]+dy[j]])
    print(b)