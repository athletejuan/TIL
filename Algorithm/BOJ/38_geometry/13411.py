N = int(input())
boom = []

for i in range(N):
    x,y,v = map(int, input().split())
    boom.append([((x**2+y**2)**.5)/v, i+1])
for j in sorted(boom):
    print(j[1])