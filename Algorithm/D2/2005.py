T = int(input())

for test_case in range(1, T+1):
    number = int(input())
    li = [1, 1]
    print(f'#{test_case}')
    if number == 1:
        print('1')
    else:
        print('1')
        print('1 1')
        while len(li) < number:
            newli = [1]
            for i in range(len(li)-1):
                newli.append(li[i] + li[i+1])
            newli.append(1)
            li = newli
            print(' '.join(list(map(str, li))))


# T = int(input())

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