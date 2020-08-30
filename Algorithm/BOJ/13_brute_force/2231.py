N = int(input())

start = N
if N < 20 and not N%2:
    start = N//2
for i in range(1, 9*len(str(N))+1):
    sn = N-i
    bn = sn
    ds = sn
    for j in range(len(str(ds))):
        ds += sn%10
        sn //= 10
    if ds == N and start > bn:
        start = bn
if start == N or start < 0:
    start = 0
print(start)