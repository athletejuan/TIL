T = int(input())

for test_case in range(1, T+1):
    number = int(input())
    num_list = list(map(int, input().split()))
    last = num_list.pop(-1)
    income = 0
    for i in range(number-1):
        ne = num_list.pop(-1)
        if last >= ne:
            income += last - ne
        else:
            last = ne
    print(f'#{test_case} {income}')