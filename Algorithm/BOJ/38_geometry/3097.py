N = int(input())
walk = []
a = b = 0
s = float('inf')
for _ in range(N):
    x,y = map(int, input().split())
    walk.append([x,y])
    a += x
    b += y
print(a,b)

for i in range(N):
    a = b = 0
    for j in range(N):
        if i!=j:
            a += walk[j][0]
            b += walk[j][1]
    dist = (a**2 + b**2)**.5
    if s > dist:
        s = dist
print('{:.2f}'.format(s))