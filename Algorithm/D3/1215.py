for tc in range(1, 11):
    N = int(input())
    board = [input() for _ in range(8)]
    count = 0

    def is_pal(x):
        if len(x) > 1:
            if x[0] == x[-1]:
                return is_pal(x[1:-1])
        else:
            return True

    for i in range(8):
        for j in range(9-N):
            row = []
            col = []
            for k in range(N):
                row.append(board[i][j+k])
                col.append(board[j+k][i])
            if is_pal(row):
                count += 1
            if is_pal(col):
                count += 1
    print('#{} {}'.format(tc, count))


# 1st try
# for test_case in range(1, 11):
#     le = int(input())
#     if le == 1:
#         print(f'#{test_case} 64')
#     count = 0
#     para = []
#     for i in range(8):
#         row = input()
#         para.extend(row.split())
#         for j in range(9-le):
#             if row[j:j+le] == row[j:j+le][::-1]:
#                 count += 1
#     for l in range(8):
#         for m in range(9-le):
#             col = []
#             for n in range(m, m+le):
#                 col.append(para[n][l])
#             print(col)
#             if col == col[::-1]:
#                 count += 1
#     print(f'#{test_case} {count}')