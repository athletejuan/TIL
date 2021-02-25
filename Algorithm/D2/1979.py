T = int(input())

def search():
    global where
    for i in range(N):
        row_poss, col_poss = 0, 0
        for j in range(N):
            # 행 방향 입력가능한 셀 합산
            if puzzle[i][j]:
                row_poss += 1
                # 행의 마지막 열에 도착했을때 입력가능한 셀의 합이 K와 같으면 where 1 추가
                if j == N-1 and row_poss == K:
                    where += 1
            else:
                # 입력 불가능한 셀이 나오는 경우 직전까지 합산한 값이 K와 같으면 where 1 추가 후 합산값 0으로 초기화
                if row_poss == K:
                    where += 1
                row_poss = 0
            if puzzle[j][i]:
                col_poss += 1
                # 열의 마지막 행에 도착했을때 입력가능한 셀의 합이 K와 같으면 where 1 추가
                if j == N-1 and col_poss == K:
                    where += 1
            else:
                # 입력 불가능한 셀이 나오는 경우 직전까지 합산한 값이 K와 같으면 where 1 추가 후 합산값 0으로 초기화
                if col_poss == K:
                    where += 1
                col_poss = 0

for tc in range(1, T+1):
    N,K = map(int, input().split())
    where = 0

    puzzle = [list(map(int, input().split())) for _ in range(N)]
    search()
    print('#{} {}'.format(tc, where))

    

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