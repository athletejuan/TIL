for tc in range(1, 11):
    N = int(input())
    bds = list(map(int, input().split()))
    view = 0
    for i in range(2, N-2):
        top, sec = 0, 0
        for idx,bd in enumerate(bds[i-2:i+3]):
            if bd > top:
                top = bd
                top_idx = idx
        if top_idx == 2:
            for idx,bd in enumerate(bds[i-2:i+3]):
                if idx == 2:
                    continue
                elif bd > sec:
                    sec = bd
            view += (top - sec)
    print('#{} {}'.format(tc, view))


# 2nd try
# for tc in range(1, 11):
#     N = int(input())
#     builds = list(map(int, input().split()))
#     view = 0
#     for i in range(2, N-2):
#         view_check = sorted(builds[i-2:i+3])
#         if builds[i] == view_check[-1]:
#             view += (builds[i] - view_check[-2])
#     print('#{} {}'.format(tc, view))


# 1st try
# for test_case in range(1, 11):
#     width = int(input())
#     height = input()
#     h_list = height.split()
#     view = 0
#     for i in range(width-4):
#         n_list = list(map(int, h_list[i:i+5]))
#         high = n_list[2]
#         if high == max(n_list):
#             n_list.pop(2)
#             view += (high - max(n_list))
#     print(f'#{test_case} {view}')