K = int(input())
directions, borders, dup, s = [], [], [], 0

for i in range(6):
    D,L = map(int, input().split())
    directions.append(D)
    borders.append(L)

for j in range(6):
    check, cnt = directions[j], 0
    for direction in directions:
        if check == direction:
            cnt += 1
    dup.append(cnt)

for k in range(5):
    if dup[k] == 2 and dup[k+1] == 1:
        s = k+1

borders = borders[s:] + borders[:s]
print((borders[0] * borders[1] - borders[3] * borders[4])*K)