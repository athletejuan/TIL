T = int(input())

def search():
    where = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            # 행 방향 입력가능한 셀 합산
            if puzzle[i][j]:
                cnt += 1
                # 0이거나 벽에 도착했을때
            if not puzzle[i][j] or j == N-1:
                # 입력가능한 셀의 합이 K와 같으면 where 1 추가
                if cnt == K:
                    where += 1
                cnt = 0
        for j in range(N):
            if puzzle[j][i]:
                cnt += 1
            if not puzzle[j][i] or  j == N-1:
                if cnt == K:
                    where += 1
                cnt = 0
    return where

for tc in range(1, T+1):
    N,K = map(int, input().split())

    puzzle = [list(map(int, input().split())) for _ in range(N)]
    print('#{} {}'.format(tc, search()))

    

# 1st try
# T = int(input())

# for test_case in range(1, T+1):
#     N, K = map(int, input().split())
#     count = 0
#     puz = []
#     for i in range(N):
#         row = list(map(int, input().split()))
#         puz.append(row)
#         for j in range(N-K+1):
#             if sum(row[j:j+K]) == K:
#                 if not j and not row[j+K]:
#                         count += 1
#                 elif j == N-K and not row[j-1]:
#                         count += 1
#                 elif not row[j-1] and not row[j+K]:
#                         count += 1
#     for k in range(N):
#         for m in range(N-K+1):
#             col = []
#             for l in range(K):
#                 col.append(puz[l+m][k])
#             if sum(col) == K:
#                 if not m and not puz[m+K][k]:
#                         count += 1
#                 elif m == N-K and not puz[m-1][k]:
#                         count += 1
#                 elif not puz[m-1][k] and not puz[m+K][k]:
#                         count += 1
#     print(f'#{test_case} {count}')