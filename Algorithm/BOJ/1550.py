hexa = input()
deci = 0

for idx, h in enumerate(hexa):
    if h.isnumeric():
        deci += 16**(len(hexa)-idx-1)*int(h)
    else:
        deci += 16**(len(hexa)-idx-1)*(ord(h)-55)
print(deci)