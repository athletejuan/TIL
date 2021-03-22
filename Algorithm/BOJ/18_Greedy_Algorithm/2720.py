T = int(input())

for _ in range(T):
    money = int(input())
    print(money // 25, end=' ')
    money %= 25
    print(money // 10, end=' ')
    money %= 10
    print(money // 5, money % 5)