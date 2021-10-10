import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
three = [0]*3

def piece(i, j, N):
    p = paper[i][j]
    for l in range(N):
        for m in range(N):
            if p != paper[i+l][j+m]:
                return False
    return True

def check(r, c, N):
    if piece(r, c, N):
        p = paper[r][c]
        three[p + 1] += 1
    else:
        for i in range(3):
            for j in range(3):
                check(r+i*N//3, c+j*N//3, N//3)

check(0, 0, N)
for i in range(3):
    print(three[i])