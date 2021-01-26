oc = list(map(int, input()))

bi = ''
for idx, n in enumerate(oc):
    if not idx and not n:
        bi = 0
        break
    temp = ''
    c = 0
    while n:
        temp = str(n % 2) + temp
        n //= 2
        c += 1
    if not idx:
        bi += temp
    else:
        bi += ('0'*(3-c) + temp)
print(bi)