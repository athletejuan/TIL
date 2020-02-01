T = int(input())

for test_case in range(1, T+1):
    number = int(input())
    result = ''
    result += '#' * number
    print(f'#{test_case} {result}')