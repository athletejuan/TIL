T = int(input())

for test_case in range(1, T+1):
    number = input()
    result = round(sum(sorted(list(map(int, number.split())))[1:-1])/(len(number.split())-2))
    print(f'#{test_case} {result}')