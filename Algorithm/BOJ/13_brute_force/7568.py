N = int(input())
bulk = [list(map(int, input().split())) for _ in range(N)]

for i in bulk:
    rank = 1
    for j in bulk:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')