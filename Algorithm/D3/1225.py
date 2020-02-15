for test_case in range(1, 11):
    T = input()
    num_list = list(map(int, input().split()))
    while num_list[7] > 0:
        i = 1
        for r in range(5):
            new = num_list.pop(0) - i
            num_list.append(new)
            if new <= 0:
                break
            i += 1
    num_list[7] = '0'
    print(f'#{T} {" ".join(list(map(str, num_list)))}')