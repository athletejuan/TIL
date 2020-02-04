T = int(input())

for test_case in range(1, T+1):
    number = input()
    print(f'#{test_case} {round(sum(map(int, number.split())) / 10)}')