T = int(input())

for test_case in range(1, T+1):
    num = input()
    if int(num[-1])%2:
        print(f'#{test_case} Odd')
    else:
        print(f'#{test_case} Even')