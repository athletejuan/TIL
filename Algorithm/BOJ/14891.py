cogs = [0] + [list(input()) for _ in range(4)]
K = int(input())
moves = [list(map(int, input().split())) for _ in range(K)]

for i in range(K):
    num, dir = moves[i][0], moves[i][1]
    lnum = rnum = num
    ldir = rdir = -dir
    left, right = cogs[num][6], cogs[num][2]
    cogs[num] = cogs[num][-dir:] + cogs[num][:-dir]

    while True:
        ln = lnum-1
        if ln > 0 and cogs[ln][2] != left:
            left, lnum = cogs[ln][6], ln
            ldir *= -1
            cogs[ln] = cogs[ln][ldir:] + cogs[ln][:ldir]
        else:
            break

    while True:
        rn = rnum+1
        if rn < 5 and cogs[rn][6] != right:
            right, rnum = cogs[rn][2], rn
            rdir *= -1
            cogs[rn] = cogs[rn][rdir:] + cogs[rn][:rdir]
        else:
            break

total = 0
for i in range(4):
    total += 2**i*int(cogs[i+1][0])
print(total)