T = int(input())

def omoc(base):
    for i in range(N):
        for j in range(N-4):
            row, col = 5, 5
            for k in range(5):
                if base[i][j+k] == 'o':
                    row -= 1
                if base[j+k][i] == 'o':
                    col -= 1
            if not row or not col:
                return 'YES' 
            for l in range(N-4-j):
                cr1, cr2, cr3, cr4 = 5, 5, 5, 5
                for m in range(5):
                    if base[j+l+m][j+m] == 'o':
                        cr1 -= 1
                    if base[j+m][j+l+m] == 'o':
                        cr2 -= 1
                    if base[j+l+m][j+(4-m)] == 'o':
                        cr3 -= 1
                    if base[j+m][j+l+(4-m)] == 'o':
                        cr4 -= 1
                if not cr1 or not cr2 or not cr3 or not cr4:
                    return 'YES'
    return 'NO'

for tc in range(1, T+1):
    N = int(input())
    base = [input() for _ in range(N)]
    print('#{} {}'.format(tc, omoc(base)))



# T = int(input())

# def omoc(base):
#     for i in range(N):
#         for j in range(N-4):
#             row, col = 5, 5
#             for k in range(N-4-j):
#                 cr1, cr2, cr3, cr4 = 5, 5, 5, 5
#                 for l in range(5):
#                     if base[i][j+l] == 'o':
#                         row -= 1
#                     if base[j+l][i] == 'o':
#                         col -= 1
#                     if base[j+k+l][j+l] == 'o':
#                         cr1 -= 1
#                     if base[j+l][j+k+l] == 'o':
#                         cr2 -= 1
#                     if base[j+k+l][j+(4-l)] == 'o':
#                         cr3 -= 1
#                     if base[j+l][j+k+(4-l)] == 'o':
#                         cr4 -= 1
#                 if not row or not col or not cr1 or not cr2 or not cr3 or not cr4:
#                     return 'YES'
#     return 'NO'

# for tc in range(1, T+1):
#     N = int(input())
#     base = [input() for _ in range(N)]
#     print('#{} {}'.format(tc, omoc(base)))