T = int(input())

for tc in range(T):
    N,M = map(int, input().split())
    d = [[0 for _ in range(M+1)] for _ in range(N)]
    for i in range(M+1):
        d[0][i] = i
    for j in range(N-1):
        for k in range(j+1, M+1):
            for l in range(j+1, k+1):
                d[j+1][k] += d[j][l-1]
    print(d[N-1][M])

# for i in range(T):
#     N,M = map(int, input().split())
#     d = [[0 for _ in range(M+1)] for _ in range(N+1)]
#     for j in range(M+1):
#         d[1][j] = j
#     for k in range(2, N+1):
#         for l in range(k, M+1):
#             for n in range(l, k-1, -1):
#                 d[k][l] += d[k-1][n-1]
#     print(d[N][M])

# for t in range(T):
#     N,M = map(int, input().split())
#     a = 1
#     b = 1
#     for i in range(N,M):
#         a *= (i+1)
#     for j in range(M-N):
#         b *= (j+1)
#     print(int(a/b))