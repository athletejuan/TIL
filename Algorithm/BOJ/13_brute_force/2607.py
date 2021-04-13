N = int(input())

origin = list(input())
similar = 0
for i in range(N-1):
    length, cnt = len(origin), 0
    atoz = {}
    for c in origin:
        if c not in atoz:
            atoz[c] = 1
        else:
            atoz[c] += 1
    word = list(input())
    for j in word:
        if j in atoz:
            atoz[j] -= 1
            length -= 1
            if not atoz[j]:
                del atoz[j]
        else:
            cnt += 1
    if length < 2 and cnt < 2:
        similar += 1
print(similar)