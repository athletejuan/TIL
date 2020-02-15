T = int(input())

for test_case in range(1, T+1):
    number = int(input())
    income = []
    for i in range(number):
        salary = list(map(float, input().split()))
        income.append(salary[0] * salary[1])
    print(f'#{test_case} {format(sum(income),".6f")}')