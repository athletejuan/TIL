N = int(input())

if N < 100:
    print(N)
elif N < 1000:
    cnt = 99
    for i in range(100, N+1):
        han1 = i%10
        han2 = (i//10)%10
        han3 = i//100
        if han3 - han2 == han2 - han1:
            cnt += 1
    print(cnt)
else:
    print(144)