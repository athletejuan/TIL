import sys
input = sys.stdin.readline

T = int(input())
ap = [500, 300, 200, 50, 30, 10]
for i in range(T):
    a,b = map(int, input().split())
    aw, bw = 0, 0
    if a and a < 22:
        n = 0
        while a > 0:
            n += 1
            a -= n
        aw = ap[n-1]
    if b and b < 32:
        m = 0
        while b > 0:
            b -= 2**m
            m += 1
        bw = 2**(10-m)
    print((aw + bw)*10000)