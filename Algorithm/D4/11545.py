T = int(input())

def TTT():
    global fin
    cro1 = base[1][1] if base[0][0] == 'T' else base[0][0]
    cro2 = base[1][2] if base[0][3] == 'T' else base[0][3]
    cro_check1 = False if cro1 == '.' else True
    cro_check2 = False if cro2 == '.' else True
    for i in range(4):
        if cro1 != base[i][i] and base[i][i] != 'T':
            cro_check1 = False
        if cro2 != base[i][3-i] and base[i][3-i] != 'T':
            cro_check2 = False
        row = base[i][1] if base[i][0] == 'T' else base[i][0]
        col = base[1][i] if base[0][i] == 'T' else base[0][i]
        row_check = False if row == '.' else True
        col_check = False if col == '.' else True
        for j in range(4):
            if base[i][j] != row and base[i][j] != 'T':
                row_check = False
            if base[i][j] == '.':
                fin = False
        for k in range(4):
            if base[k][i] != col and base[k][i] != 'T':
                col_check = False
        if row_check:
            return row
        elif col_check:
            return col
    if cro_check1:
        return cro1
    elif cro_check2:
        return cro2

for tc in range(1, T+1):
    base = [input() for _ in range(4)]
    if tc < T:
        skip = input()
    fin = True

    winner = TTT()
    if winner:
        print('#{} {} won'.format(tc, winner))
    elif fin:
        print('#{} Draw'.format(tc))
    else:
        print('#{} Game has not completed'.format(tc))


# T = int(input())
#
# def TTT():
#     global fin
#     cro1 = base[1][1] if base[0][0] == 'T' else base[0][0]
#     cro2 = base[1][2] if base[0][3] == 'T' else base[0][3]
#     cro_check1 = False if cro1 == '.' else True
#     cro_check2 = False if cro2 == '.' else True
#     for i in range(4):
#         if cro1 != base[i][i] and base[i][i] != 'T':
#             cro_check1 = False
#         if cro2 != base[i][3-i] and base[i][3-i] != 'T':
#             cro_check2 = False
#         row = base[i][1] if base[i][0] == 'T' else base[i][0]
#         col = base[1][i] if base[0][i] == 'T' else base[0][i]
#         row_check = False if row == '.' else True
#         col_check = False if col == '.' else True
#         for j in range(4):
#             if base[i][j] == '.':
#                 ing = True
#                 break
#             else:
#                 if base[i][j] != row and base[i][j] != 'T':
#                     break
#         else:
#             return row
#         for k in range(4):
#             if base[k][i] == '.':
#                 ing = True
#                 break
#             else:
#                 if base[k][i] != col and base[k][i] != 'T':
#                     break
#         else:
#             return col
#     else:
#         if cro_check1:
#             return cro1
#         elif cro_check2:
#             return cro2
#         elif not ing:
#             fin = True
#
# for tc in range(1, T+1):
#     base = [input() for _ in range(4)]
#     if tc < T:
#         skip = input()
#     fin = False
#
#     winner = TTT()
#     if winner:
#         print('#{} {} won'.format(tc, winner))
#     elif fin:
#         print('#{} Draw'.format(tc))
#     else:
#         print('#{} Game has not completed'.format(tc))