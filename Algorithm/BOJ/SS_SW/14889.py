N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
diff = 50*N

def vs(a,b,half):
    global diff
    start = link = 0
    for i in range(half-1):
        for j in range(i, half):
            start += S[a[i]][a[j]] + S[a[j]][a[i]]
            link += S[b[i]][b[j]] + S[b[j]][b[i]]
    if diff > abs(start - link):
        diff = abs(start - link)


def combination(half):
    for i in range(1, 2**N):
        cnt, start, link = 0, [], []
        for j in range(N):
            if i & (1 << j):
                cnt += 1
                start.append(j)
            else:
                link.append(j)
        if cnt == half:
            vs(start, link, half)

combination(N//2)
print(diff)