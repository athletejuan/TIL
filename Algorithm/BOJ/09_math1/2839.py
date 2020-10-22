N = int(input())

five = N//5
for i in range(five):
    if not (N - (five-i)*5)%3:
        print(five-i + ((N-(five-i)*5)//3))
        break
else:
    if not N%3:
        print(N//3)
    else:
        print(-1)