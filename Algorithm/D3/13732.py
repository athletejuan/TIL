T = int(input())
 
 
def square(r,c):
    global flag
    s = c
    while s < N and matrix[r][s] == '#':
        s += 1
    for k in range(s-c):
        for l in range(s-c):
            if r+k < N and c+l < N and matrix[r+k][c+l] == '#':
                matrix[r+k][c+l] = '.'
            else:
                return False
    flag = True
    return True
 
 
def check():
    global flag
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == '#':
                if not flag and square(i,j):
                    flag = True
                else:
                    flag = False
                    return
 
 
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(input()) for _ in range(N)]
    flag = False
 
    check()
    flag = 'yes' if flag else 'no'
    print(f'#{tc} {flag}')