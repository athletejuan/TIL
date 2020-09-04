T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    cubic = []
    for _ in range(N):
        cubic.append(list(map(int, input().split())))
    rotate = [[0]*3*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rotate[j][N-1-i] = rotate[N-1-i][2*N-1-j] = rotate[N-1-j][2*N+i] = cubic[i][j]
    print(f'#{test_case}')
    for _ in range(N):
        print(''.join(map(str, rotate[_][:N])) + ' ' + ''.join(map(str, rotate[_][N:2*N])) + ' ' + ''.join(map(str, rotate[_][2*N:])))