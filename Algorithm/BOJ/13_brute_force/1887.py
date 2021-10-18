T,N = map(int, input().split())
constraints = [list(map(int, input().split()))[1:] for _ in range(N)]
ban, cnt = [], 0

for i in range(N):
    convert = 0
    for j in constraints[i]:
        convert += 2**(j-1)
    ban.append(convert)

for i in range(1 << T):
    for b in ban:
        if b & i == b:
            break
    else:
        cnt += 1
print(cnt)