bi = input()

oc = ''
for i in range((len(bi)+2)//3):
    t = 0
    for idx, j in enumerate(bi[-i*3-1:-i*3-4:-1]):
        if j == '1':
            t += 2 ** idx
    oc = str(t) + oc
print(oc)


# binary -> decimal -> octa
# 시간초과
# de = 0
# oc = ''
# for i, b in enumerate(bi):
#     if int(b):
#         de += 2 ** (len(bi)-1-i)
# while de:
#     re = de % 8
#     de //= 8
#     oc = str(re) + oc

# if not oc:
#     print(0)
# else:
#     print(oc)