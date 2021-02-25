T = int(input())

def row_col(x):
    row_sum, col_sum, dup_row, dup_col = 0, 0, [], []
    for i in range(9):
        # 행,열 방향 합산 45 확인
        row_sum += sudoku[x][i]
        col_sum += sudoku[i][x]
        # 행,열 방향 중복 확인
        if sudoku[x][i] not in dup_row:
            dup_row.append(sudoku[x][i])
        if sudoku[i][x] not in dup_col:
            dup_col.append(sudoku[i][x])
    return 1 if len(dup_row) == len(dup_col) == 9 and row_sum == col_sum == 45 else 0

def cube(x, y):
    # 3x3 큐브안의 항목들의 중복 여부와 합이 45인지 확인
    cube_sum, dup_cube = 0, []
    for i in range(x, x+3):
        for j in range(y, y+3):
            cube_sum += sudoku[i][j]
            # 중복 여부 확인
            if sudoku[i][j] not in dup_cube:
                dup_cube.append(sudoku[i][j])
    return 1 if cube_sum == 45 and len(dup_cube) == 9 else 0

for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    result = 1
    # 행,열 합산 및 중복 여부 확인
    for i in range(9):
        if not row_col(i):
            result = 0
    # 3x3 큐브의 합산 및 중복 여부 확인
    for j in range(3):
        for k in range(3):
            if not cube(3*j, 3*k):
                result = 0
    print('#{} {}'.format(tc, result))
    


# 1st try
# T = int(input())

# for test_case in range(1, T+1):
#     sudoku = []
#     sum_cube = []
#     result = 1
#     for i in range(3):
#         cube = []
#         for j in range(3):
#             row = list(map(int, input().split()))
#             sudoku.append(row)
#             if sum(row) != 45:
#                 result = 0
#             for k in range(3):
#                 cube.append(sum(row[3*k:3*(k+1)]))
#         sum_cube.append(cube)
#         sc = 0
#         for b in range(3):
#             sc += sum_cube[i][(3*b)+i]
#         if sc != 45:
#             result = 0
#     for l in range(9):
#         cs = 0
#         for m in range(9):
#             cs += sudoku[m][l]
#         if cs != 45:
#             result = 0
#     if result:
#         for a in range(9):
#             num_check = []
#             for c in range(9):
#                 if len(set(sudoku[c])) != 9:
#                     result = 0
#                 num_check.append(sudoku[c][a])
#             if len(set(num_check)) != 9:
#                 result = 0
#         for d in range(3):
#             for e in range(3):
#                 tri = []
#                 for f in range(3):
#                     for g in range(3):
#                         tri.append(sudoku[(d*3)+f][(3*e)+g])
#                 if len(set(tri)) != 9:
#                     result = 0
#     print(f'#{test_case} {result}')