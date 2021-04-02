N = int(input())

A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

for i in range(N):
    for j in range(N):
        for k in range(N):
            if A[i][k] and B[k][j]:
                cnt += 1
                break
print(cnt)