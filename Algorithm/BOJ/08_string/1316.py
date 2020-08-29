N = int(input())

cnt = 0
for _ in range(N):
    word = input()
    dup = []
    for i in word:
        if not dup or i not in dup:
            dup.append(i)
        elif i in dup[:-1]:
            break
    else:
        cnt += 1
print(cnt)