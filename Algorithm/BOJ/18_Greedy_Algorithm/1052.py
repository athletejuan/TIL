N,K = map(int, input().split())
bottle = cnt = buy = 0
B = N

while B:
    cnt += 1
    B,R = divmod(B, 2)
    if R:
        bottle += 1


if bottle > K:
    bottle, buy = 0, 1
    for i in range(cnt):
        if bottle < K:
            if N & 1 << cnt-i-1:
                bottle += 1
        else:
            if not N & 1 << cnt-i-1:
                buy += 2**(cnt-i-1)

print(buy)