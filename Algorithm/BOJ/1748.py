N = input()

if len(N) == 1:
    print(N)
else:
    count = 0
    for i in range(len(N)-1):
        count += (i+1)*9*(10**i)
    count += (i+2)*(int(N) - (10**(i+1)) + 1)
    print(count)