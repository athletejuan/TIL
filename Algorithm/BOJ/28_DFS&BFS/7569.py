def tomato():
    for i in range(N*H):
        for j in range(M):
            if not boxes[i][j]:
                return
    return True


def BFS(q):
    cnt = 0
    while True:
        temp = []
        while q:
            r,c = q.pop()
            for i in range(6):
                nr, nc = r + dr[i], c + dc[i]
                if i < 2:
                    if N*(r//N) <= nr < N*(r//N+1) and 0 <= nc < M and not boxes[nr][nc]:
                        temp.append([nr, nc])
                        boxes[nr][nc] = 1
                elif 0 <= nr < N*H and 0 <= nc < M and not boxes[nr][nc]:
                    temp.append([nr, nc])
                    boxes[nr][nc] = 1
        if temp:
            q = temp
            cnt += 1
        else:
            return cnt


M,N,H = map(int, input().split())
boxes = [list(map(int, input().split())) for _ in range(N*H)]
dr, dc = [1, -1, 0, 0, -N, N], [0, 0, 1, -1, 0, 0]
q = []
for i in range(N*H):
    for j in range(M):
        if boxes[i][j] > 0:
            q.append([i, j])
day = BFS(q)
print(day if tomato() else -1)