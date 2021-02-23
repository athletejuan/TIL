T = int(input())

for tc in range(T):
    ex = input().split()
    for i in range(len(ex)):
        if not i:
            mars = float(ex[i])
        else:
            if ex[i] == '@':
                mars *= 3
            elif ex[i] == '%':
                mars += 5
            else:
                mars -= 7
    print(format(mars, ".2f"))