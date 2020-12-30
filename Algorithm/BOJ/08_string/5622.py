word = input()
time = 0

for c in word:
    if (ord(c)+1)//3 < 28:
        time += (ord(c)+1)//3 - 19
    elif c == 'Z':
        time += 10
    else:
        time += (ord(c)//3) - 19
print(time)