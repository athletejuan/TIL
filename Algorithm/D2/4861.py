T = int(input())

for test_case in range(1, T+1):
    N,M = map(int, input().split())
    pal = []
    for i in range(N):
        char = input()
        for j in range(N-M+1):
            if char[j:j+M] == char[j:j+M][::-1]:
                print(f'#{test_case} {char[j:j+M]}')
                break
        pal.append(char)
    for k in range(N):
        for l in range(N-M+1):
            col = ''
            for m in range(l,M+l):
                col += pal[m][k]
            if col == col[::-1]:
                print(f'#{test_case} {col}')
                break