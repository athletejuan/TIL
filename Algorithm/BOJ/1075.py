N = int(input())
F = int(input())
a = 0

while True:
    if not ((N//100)*100 + a)%F:
        if a < 10:
            print('0'+str(a))
        else:
            print(a)
        break
    a += 1