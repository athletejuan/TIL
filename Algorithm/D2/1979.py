T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    count = 0
    puz = []
    for i in range(N):
        row = list(map(int, input().split()))
        puz.append(row)
        for j in range(N-K+1):
            if sum(row[j:j+K]) == K:
                if not j and not row[j+K]:
                        count += 1
                elif j == N-K and not row[j-1]:
                        count += 1
                elif not row[j-1] and not row[j+K]:
                        count += 1
    for k in range(N):
        for m in range(N-K+1):
            col = []
            for l in range(K):
                col.append(puz[l+m][k])
            if sum(col) == K:
                if not m and not puz[m+K][k]:
                        count += 1
                elif m == N-K and not puz[m-1][k]:
                        count += 1
                elif not puz[m-1][k] and not puz[m+K][k]:
                        count += 1
    print(f'#{test_case} {count}')