N = int(input())

def fac(N):
    if N < 2:
        return 1
    else:
        return fac(N-1)*N

cnt = 0
num = fac(N)
while True:
    if num%10:
        print(cnt)
        break
    else:
        num //= 10
        cnt += 1