N = int(input())

ans = 100
cnt = 0
while ans != N:
    if not cnt:
        ans = N
    if ans < 10:
        ans *= 11
    else:
        ans = (ans%10)*10+((ans//10+ans%10)%10)
    cnt += 1
print(cnt)