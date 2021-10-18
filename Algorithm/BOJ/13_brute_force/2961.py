N = int(input())
ingredients = [list(map(int, input().split())) for _ in range(N)]


def DY(taste):
    for i in range(1, 1 << N):
        sub, sour, bitter = [], 1, 0
        for j in range(i):
            if i & (1 << j):
                sub.append(ingredients[j])
        for s,b in sub:
            if s == b:
                return 0
            sour *= s
            bitter += b
        else:
            if sour < bitter:
                sour, bitter = bitter, sour
            if not taste or sour - bitter < taste:
                taste = sour - bitter
    return taste
print(DY(0))