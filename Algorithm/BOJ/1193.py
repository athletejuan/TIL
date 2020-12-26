X = int(input())

f = 0
i = 0
while f < X:
    i += 1
    f += i
r = X-(f-i)
if i%2:
    print(f'{i-r+1}/{r}')
else:
    print(f'{r}/{i-r+1}')