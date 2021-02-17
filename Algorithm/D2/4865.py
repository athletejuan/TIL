T = int(input())

for tc in range(1, T+1):
    N = set(list(input()))
    M = input()
    str_cnt = {}
    max_val = 0

    for n in N:
        for m in M:
            if n == m:
                if n in str_cnt:
                    str_cnt[n] += 1
                else:
                    str_cnt[n] = 1

    for value in str_cnt.values():
        if value > max_val:
            max_val = value
    print('#{} {}'.format(tc, max_val))


# 1st try
# for test_case in range(1, T+1):
#     str1 = input()
#     str2 = input()

#     rank = 0
#     for i in str1:
#         if str2.count(i) > rank:
#             rank = str2.count(i)
#     print(f'#{test_case} {rank}')