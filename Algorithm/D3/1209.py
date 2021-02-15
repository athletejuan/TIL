for _ in range(10):
    tc = input()
    arr = []
    col = [0]*102
    for i in range(100):
        row = list(map(int, input().split()))
        arr.append(sum(row))
        col[100] += row[i]
        col[101] += row[99-i]
        for j in range(100):
            col[j] += row[j]
    total = arr + col
    print(f'#{tc} {max(total)}')


# 1st try

# for t in range(1, 11):
#     test_case = input()
#     sum_list = []
#     total = []
#     count1 = 0
#     count2 = 99
#     cross1 = []
#     cross2 = []
#     for i in range(100):
#         width = list(map(int, input().split()))
#         sum_list.append(sum(width))
#         total.extend(width)
#     for j in range(100):
#         height = []
#         for idx, num in enumerate(total):
#             if idx % 100 == j:
#                 height.append(num)
#         sum_list.append(sum(height))
#     for k in range(100):
#         for idx, num in enumerate(total):
#             if idx == count1:
#                 cross1.append(num)
#                 count1 += 101
#     sum_list.append(sum(cross1))
#     for l in range(100):
#         for idx, num in enumerate(total):
#             if idx == count2:
#                 cross2.append(num)
#                 count2 += 99
#     sum_list.append(sum(cross2))
#     print(f'#{test_case} {max(sum_list)}')