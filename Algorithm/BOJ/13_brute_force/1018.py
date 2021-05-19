N,M = map(int, input().split())
board = []

for _ in range(N):
    board.append(list(input()))

array = []
for i in range(N-7):
    for j in range(M-7):
        count = 0
        for k in range(4):
            for l in range(4):
                if board[i+2*k][j+2*l] != board[i][j]:
                    count += 1
                if board[i+2*k+1][j+2*l] == board[i][j]:
                    count += 1
                if board[i+2*k][j+2*l+1] == board[i][j]:
                    count += 1
                if board[i+2*k+1][j+2*l+1] != board[i][j]:
                    count += 1
        if count > 64 - count:
            count = 64 - count
        array.append(count)
print(min(array))