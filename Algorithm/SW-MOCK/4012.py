# 사용여부 체크 형태로 순열 구하면 시간초과

def cook(forA, forB, half):
    A = B = 0
    for i in range(half-1):
        for j in range(i, half):
            A += ingredients[forA[i]][forA[j]] + ingredients[forA[j]][forA[i]]
            B += ingredients[forB[i]][forB[j]] + ingredients[forB[j]][forB[i]]
    return abs(A-B)


def combination(half):
    global similar
    for i in range(1, 2**N):
        cnt, used, unused = 0, [], []
        for j in range(N):
            if i & (1 << j):
                cnt += 1
                used.append(j)
            else:
                unused.append(j)
        if cnt == half:
            gap = cook(used, unused, cnt)
            if gap < similar:
                similar = gap


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ingredients = [list(map(int, input().split())) for _ in range(N)]
    similar = 10000 * N

    combination(N//2)
    print('#{} {}'.format(tc, similar))