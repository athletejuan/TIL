M = int(input())
N = int(input())
S = int(M**.5)
check = S**2
PS = 0

while check <= N:
    if M <= check <= N:
        if not PS:
            mini = check
        PS += check
    S += 1
    check = S**2
if PS:
    print(PS)
    print(mini)
else:
    print(-1)
