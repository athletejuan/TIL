N = int(input())

origin = list(input())
for _ in range(N-1):
    f = list(input())
    for c in range(len(origin)):
        if origin[c] != f[c]:
            origin[c] = '?'
print(''.join(origin))