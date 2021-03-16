N,M = map(int, input().split())

DNA = [input() for _ in range(N)]
HD = 0
for i in range(M):
    check = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    for j in range(N):
        check[DNA[j][i]] += 1
    HD += N-sorted(check.values())[-1]
    print(sorted(check.items(), key=lambda x: (-x[1], x[0]))[0][0], end='')
print()
print(HD)