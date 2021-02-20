N = int(input())
maxwin = 0

for _ in range(N):
    a,b,c = map(int, input().split())

    prize = 1000+a*100
    if a == b:
        if a == c:
            prize = 10000+a*1000
    else:
        if b == c:
            prize = 1000+b*100
        elif a != c:
            if a < b:
                a,b = b,a
            if a < c:
                prize = c*100
            else:
                prize = a*100
    if maxwin < prize:
        maxwin = prize
print(maxwin)