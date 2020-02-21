T = int(input())

for test_case in range(1, T+1):
    numbers = input()
    num_list = []
    c_num = []
    count = 1
    for num in numbers:
        num_list.append(num)
    for i in num_list[::-1]:
        if not c_num:
            c_num.append(i)
        elif i != c_num[-1]:
            c_num.append(i)
            count += 1
    if i == '0':
        count -= 1
    print(f'#{test_case} {count}')