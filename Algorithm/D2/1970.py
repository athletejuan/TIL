T = int(input())

for test_case in range(1, T+1):
    number = int(input())/10
    change = []
    for i in range(3):
        num = number % 10
        a = num // 5
        b = num % 5
        change.insert(0, round(b))
        change.insert(0, round(a))
        number = number // 10
    a = number // 5
    b = number % 5
    change.insert(0, round(b))
    change.insert(0, round(a))
    print(f'#{test_case}')
    print(' '.join(list(map(str, change))))