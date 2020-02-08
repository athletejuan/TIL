for test_case in range(1, 11):
    count = int(input())
    height = input()
    h_list = sorted(list(map(int, height.split())))
    for i in range(count):
        high = h_list.pop()
        low = h_list.pop(0)
        # gap = high - low
        high -= 1
        low += 1
        h_list.append(high)
        h_list.append(low)
        gap = max(h_list) - min(h_list)
        if gap <= 1:
            print(f'#{test_case} {gap}')
            break
        h_list.sort()
    else:
        print(f'#{test_case} {gap}')