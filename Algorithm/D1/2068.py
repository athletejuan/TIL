T = int(input())

for test_case in range(1, T+1):
    number = input()
    print(f'#{test_case} {max(map(int, number.split()))}')