T = int(input())

def perm(start, now):
    global cnt, total
    for i in range(1,N):
        if i != start and not visited[i]:
            cnt += 1
            now += base[start][i]
            visited[i] = 1
            if cnt == N-1:
                now += base[i][0]
                if not total or total > now:
                    total = now
            perm(i, now)
            now -= base[start][i]
            cnt -= 1
            visited[i] = 0

for tc in range(1, T+1):
    N = int(input())
    base = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    cnt, total = 0, 0
    perm(0, 0)
    print('#{} {}'.format(tc, total))


# 순서 상관없이 중복된 행,열 없이 최소값 찾기
# def perm(cnt, now):
#     global total
#     for i in range(cnt, N):
#         for j in range(N):
#             if i != j and not visited[j]:
#                 cnt += 1
#                 now += base[i][j]
#                 visited[j] = 1
#                 if cnt == N:
#                     if not total or total > now:
#                         total = now
#                 perm(cnt, now)
#                 now -= base[i][j]
#                 cnt -= 1
#                 visited[j] = 0
#         else:
#             break
