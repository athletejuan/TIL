for test_case in range(1, 11):
    width = int(input())
    height = input()
    h_list = height.split()
    view = 0
    for i in range(width-4):
        n_list = list(map(int, h_list[i:i+5]))
        high = n_list[2]
        if high == max(n_list):
            n_list.pop(2)
            view += (high - max(n_list))
    print(f'#{test_case} {view}')