N = int(input())

P = sorted(list(map(int, input().split())))
t = 0
w = 0
for p in P:
    w += p
    t += w
print(t)