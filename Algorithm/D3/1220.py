for tc in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        flag = False
        for j in range(N):
            if table[j][i]:
                if not flag and table[j][i] % 2:
                    flag = True
                elif flag and not table[j][i] % 2:
                    flag = False
                    cnt += 1
    print('#{} {}'.format(tc, cnt))


# 1st try
# for test_case in range(1, 11):
#     N = int(input())
#     table = []
#     count = 0
#     for i in range(N):
#         table.append(input().split())
#     for num in range(N):
#         col = []
#         for row in table:
#             if int(row[num]):
#                 col.append(row[num])
#         for i in range(len(col)-1):
#             if col[i] == '1' and col[i+1] == '2':
#                 count += 1
#     print(f'#{test_case} {count}')