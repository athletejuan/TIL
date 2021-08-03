n = int(input())

coin = 0
five = n//5
if not five and n%2:
    print(-1)
else:
    if (n - 5*five)%2:
        five -= 1
    n -= 5*five
    coin += five+n//2
    print(coin)