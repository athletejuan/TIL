N,K,L = map(int, input().split())
K -= 1
L -= 1
rnd = 1

while K//2 != L//2:
    rnd += 1
    K //= 2
    L //= 2

print(rnd)