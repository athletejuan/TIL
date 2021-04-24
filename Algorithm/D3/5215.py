T = int(input())

def DFS(x, flavor, cal):
    global best
    used[x] = 1
    flavor += gre[x][0]
    cal += gre[x][1]
    if cal > L:
        return
    if best < flavor:
        best = flavor
    for i in range(x, N):
        if not used[i]:
            DFS(i, flavor, cal)
            used[i] = 0

for tc in range(1, T+1):
    N,L = map(int, input().split())
    gre = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    best = 0

    for i in range(N):
        DFS(i, 0, 0)

    print('#{} {}'.format(tc, best))


# aclass
# def perm(idx):
#     global max_score
#     if idx == N:
#         total_calorie = total_score = 0
#         for i in range(N):
#             if checks[i]:
#                 total_calorie += scores[i][1]
#                 if total_calorie > limit:
#                     return
#                 total_score += scores[i][0]
#         if total_score > max_score:
#             max_score = total_score
#         return
#     checks[idx] = True
#     perm(idx + 1)
#     checks[idx] = False
#     perm(idx + 1)
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, limit = map(int, input().split())
#     scores = []
#     checks = [None for _ in range(N)]
#     for _ in range(N):
#         # (점수, 칼로리)
#         scores.append(tuple(map(int, input().split())))
#     max_score = 0
#     perm(0)
#     print(f"#{tc} {max_score}")


# 시간초과
# for tc in range(1, T+1):
#     N,L = map(int, input().split())
#     gre = [list(map(int, input().split())) for _ in range(N)]
#     best = 0
#
#     for i in range(1<<N):
#         flavor = limit = 0
#         for j in range(i):
#             if i & (1<<j):
#                 limit += gre[j][1]
#                 if limit > L:
#                     break
#                 flavor += gre[j][0]
#         if best < flavor:
#             best = flavor
#     print('#{} {}'.format(tc, best))