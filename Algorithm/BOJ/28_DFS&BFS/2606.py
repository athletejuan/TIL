C = int(input())
L = int(input())
M = [[0]*(C+1) for _ in range(C+1)]
for _ in range(L):
    x,y = map(int, input().split())
    M[x][y] = M[y][x] = 1
visit = [0]*(C+1)
cnt = 0

def virus(s):
    queue = [s]
    visit[s] = 1
    while queue:
        s = queue.pop(0)
        for i in range(1, C+1):
            if M[s][i] and not visit[i]:
                queue.append(i)
                visit[i] = 1
                global cnt
                cnt += 1

virus(1)
print(cnt)