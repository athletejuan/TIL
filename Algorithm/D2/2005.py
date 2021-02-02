T = int(input())

for test_case in range(1, T+1):
    number = int(input())
    li = [0, 1, 0]
    print(f'#{test_case}')
    while len(li) < number+3:
        print(' '.join(list(map(str, li[1:-1]))))
        newli = [0]
        for i in range(len(li)-1):
            newli.append(li[i] + li[i+1])
        newli.append(0)
        li = newli

# 2중 리스트
# for t in range(T):
#     print('#{}'.format(t+1))
#     print(f'{t+1}')
#     num = int(input())
#     pascal = [[0 for n in range(num)] for nu in range(num)]
#     for i in range(num):
#         pascal[i][0] = 1
#         pascal[i][i] = 1
#     for i in range(2, num):
#         for j in range(1, i):
#             pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
#     for i in range(num):
#         for j in range(num):
#             print(pascal[i][j], end=' ') if pascal[i][j] != 0 else print('', end='')
#         print('')