def is_pal(x):
    if len(x) > 1:
        if x[0] == x[-1]:
            return is_pal(x[1:-1])
    else:
        return True

def check(board):
    for i in range(100):
        for j in range(100):
            for k in range(i+1):
                row = []
                col = []
                for l in range(100-i):
                    row.append(board[j][i-k+l])
                    col.append(board[i-k+l][j])
                if is_pal(row) or is_pal(col):
                    return '#{} {}'.format(tc, l+1)

for _ in range(10):
    tc = input()
    board = [input() for _ in range(100)]
    print(check(board))