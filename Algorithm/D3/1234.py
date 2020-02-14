for test_case in range(1, 11):
    numbers = input().split()[1]
    num_list = []
    i = 0
    for a in numbers:
        num_list.append(a)
    while i < len(num_list)-1:
        if num_list[i] == num_list[i+1]:
            num_list.pop(i)
            num_list.pop(i)
            i = -1
        i += 1
    print(f"#{test_case} {''.join(num_list)}")