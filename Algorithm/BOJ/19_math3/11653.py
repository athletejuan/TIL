N = int(input())

for i in range(2, N+1):
    if not N%i:
        while not N%i:
            N//=i
            print(i)