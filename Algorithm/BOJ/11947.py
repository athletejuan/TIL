T = int(input())

for tc in range(1, T+1):
    N = int(input())
    C = N
    cnt = -1
    while C:
        C //= 10
        cnt += 1
    lovely = min(5*(10**cnt), N)
    print(lovely*(10**(cnt+1)-lovely-1))