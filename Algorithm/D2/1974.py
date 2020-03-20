T = int(input())

for test_case in range(1, T+1):
    sudoku = []
    sum_cube = []
    result = 1
    for i in range(3):
        cube = []
        for j in range(3):
            row = list(map(int, input().split()))
            sudoku.append(row)
            if sum(row) != 45:
                result = 0
            for k in range(3):
                cube.append(sum(row[3*k:3*(k+1)]))
        sum_cube.append(cube)
        sc = 0
        for b in range(3):
            sc += sum_cube[i][(3*b)+i]
        if sc != 45:
            result = 0
    for l in range(9):
        cs = 0
        for m in range(9):
            cs += sudoku[m][l]
        if cs != 45:
            result = 0
    if result:
        for a in range(9):
            num_check = []
            for c in range(9):
                if len(set(sudoku[c])) != 9:
                    result = 0
                num_check.append(sudoku[c][a])
            if len(set(num_check)) != 9:
                result = 0
        for d in range(3):
            for e in range(3):
                tri = []
                for f in range(3):
                    for g in range(3):
                        tri.append(sudoku[(d*3)+f][(3*e)+g])
                if len(set(tri)) != 9:
                    result = 0
    print(f'#{test_case} {result}')



# for test_case in range(1, T+1):
#     sudoku = []
#     for i in range(3):
#         cube = []
#         for j in range(3):
#             row = list(map(int, input().split()))
#             sudoku.append(row)
#             if sum(row) != 45:
#                 print(f'#{test_case} 0')
#                 break
#             t = []
#             for k in range(3):
#                 t.append(sum(row[(3*k):((3*k)+3)]))
#             cube.append(t[(3*j)+i])
#         if sum(cube) != 45:
#             print(f'#{test_case} 0')
#             break
#     for l in range(9):
#         col = []
#         for m in range(9):
#             col.append(sudoku[m][l])
#         if sum(col) != 45:
#             print(f'#{test_case} 0')
#             break
#     else:
#         print(f'#{test_case} 1')


# for test_case in range(1, T+1):
#     sudoku = []
#     for i in range(9):
#         row = list(map(int, input().split()))
#         sudoku.append(row)
#         if sum(row) != 45:
#             print(f'#{test_case} 0')
#             break
#     for j in range(9):
#         col = []
#         for k in range(9):
#             col.append(sudoku[j][k])
#         if sum(col) != 45:
#             print(f'#{test_case} 0')
#             break
#     t_cube = []
#     for a in range(3):  
#         for b in range(3):
#             cube = []
#             for c in range(3):
#                 for d in range(3):
#                     cube.append(sudoku[(a*3)+c][(3*b)+d])
#             t_cube.append(cube)
#     for e in t_cube:
#         if sum(e) != 45:
#             print(f'#{test_case} 0')
#             break
#     else:
#         print(f'#{test_case} 1')




# for test_case in range(1, T+1):
#     sudoku = []
#     t_cube = []
#     result = 1
#     for i in range(9):
#         row = list(map(int, input().split()))
#         sudoku.append(row)
#         if sum(row) != 45:
#             result = 0
#         cube = []
#         for j in range(3):
#             cube.append(sum(row[(3*j):(3*j)+3]))
#         t_cube.append(cube)
#     pprint(t_cube)
#     for k in range(3):
#         sc = 0
#         for l in range(3):
#             for m in range(3):
#                 sc += t_cube[m+(3*k)][l]
#                 if sc != 45:
#                     result = 0
#     for a in range(9):
#         col = []
#         for b in range(9):
#             col.append(sudoku[a][b])
#         if sum(col) != 45:
#             result = 0
#     print(f'#{test_case} {result}')