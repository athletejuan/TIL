for T in range(1, 11):
    count = input()
    calc = input()
    num_list = []
    for i in calc:
        num_list.append(i)
    num_list.append(num_list.pop(1))
    re = ''.join(num_list)[1:] + ''.join(num_list)[0]
    numbers = list(map(int, re.split('+')))
    print(f'#{T} {sum(numbers)}')