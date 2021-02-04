E,S,M = map(int, input().split())

Y = 1
while True:
    if Y % 15 == E and Y % 28 == S and Y % 19 == M:
        print(Y)
        break
    elif E == 15 or S == 28 or M == 19:
        if Y % 15 == E-1 and Y % 28 == S-1 and Y % 19 == M-1:
            print(Y+1)
            break
    Y += 1