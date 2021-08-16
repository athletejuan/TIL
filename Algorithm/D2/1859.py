T = int(input())

for tc in range(1, T+1):
    N = int(input())
    daily = list(map(int, input().split()))
    asset, i = 0, 1
    top = daily[-1]
    while i < len(daily):
        if daily[-1-i] > top:
            top = daily[-1-i]
            daily = daily[:-i]
            i = 1
        else:
            asset += (top-daily[-1-i])
            i += 1
    print('#{} {}'.format(tc, asset))


# 1st try
# for test_case in range(1, T+1):
#     number = int(input())
#     num_list = list(map(int, input().split()))
#     last = num_list.pop(-1)
#     income = 0
#     for i in range(number-1):
#         ne = num_list.pop(-1)
#         if last >= ne:
#             income += last - ne
#         else:
#             last = ne
#     print(f'#{test_case} {income}')