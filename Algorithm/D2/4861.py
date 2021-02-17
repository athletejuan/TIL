T = int(input())

def is_pal(x):
    if len(x) > 1:
        if x[-1] == x[0]:
            return is_pal(x[1:-1])
    else:
        return True    

def check(board, N, M):
    for i in range(N):
        for j in range(N-M+1):
            row = []
            col = []
            for k in range(M):
                row.append(board[i][j+k])
                col.append(board[j+k][i])
            if is_pal(row):
                return row
            if is_pal(col):
                return col

for tc in range(1, T+1):
    N,M = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    print('#{} {}'.format(tc, ''.join(check(board, N, M))))


# 1st try
# for test_case in range(1, T+1):
#     N,M = map(int, input().split())
#     pal = []
#     for i in range(N):
#         char = input()
#         for j in range(N-M+1):
#             if char[j:j+M] == char[j:j+M][::-1]:
#                 print(f'#{test_case} {char[j:j+M]}')
#                 break
#         pal.append(char)
#     for k in range(N):
#         for l in range(N-M+1):
#             col = ''
#             for m in range(l,M+l):
#                 col += pal[m][k]
#             if col == col[::-1]:
#                 print(f'#{test_case} {col}')
#                 break