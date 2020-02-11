for t in range(1, 11):
    test_case = input()
    sum_list = []
    total = []
    count1 = 0
    count2 = 99
    cross1 = []
    cross2 = []
    for i in range(100):
        width = list(map(int, input().split()))
        sum_list.append(sum(width))
        total.extend(width)
    for j in range(100):
        height = []
        for idx, num in enumerate(total):
            if idx % 100 == j:
                height.append(num)
        sum_list.append(sum(height))
    for k in range(100):
        for idx, num in enumerate(total):
            if idx == count1:
                cross1.append(num)
                count1 += 101
    sum_list.append(sum(cross1))
    for l in range(100):
        for idx, num in enumerate(total):
            if idx == count2:
                cross2.append(num)
                count2 += 99
    sum_list.append(sum(cross2))
    print(f'#{test_case} {max(sum_list)}')