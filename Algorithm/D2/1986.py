T = int(input())

for test_case in range(1, T+1):
    number = int(input())
    if number % 2:
        result = (number + 1) // 2
    else:
        result = (number * -1) // 2
    print(f'#{test_case} {result}')