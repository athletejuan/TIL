T = int(input())

for tc in range(1, T+1):
    N = int(input())
    harvest = 0
    for i in range(N):
        row = list(map(int, list(input())))
        if i <= N//2:
            harvest += sum(row[N//2-i:N//2+i+1])
        else:
            harvest += sum(row[-(N//2)+i:N-(i-N//2)])
    print(f'#{tc} {harvest}')


# Ed
# import sys
# sys.stdin = open('input.txt', 'r')

# T = int(input())

# for test_case in range(1, T+1):
#     N = int(input())

#     center = (N // 2) + 1
#     dr = 0
#     res = 0
#     for row in range(N):
#         arr = list(map(int, list(input())))

#         dr += 1 if row//center else -1
#         res += sum(arr[center+dr : center-dr-1])

#     print('#{} {}'.format(test_case, res))


# 1st try

# for test_case in range(1, T+1):
#     n = int(input())
#     answer = 0
#     for i in range(n):
#         row = input()
#         str_list = []
#         for j in row:
#             str_list.append(j)
#         num_list = list(map(int, str_list))
#         if i > (n//2):
#             answer += sum(num_list[((n//2)-(i-(2*(i-(n//2))))):((n//2)+(i+1)-(2*(i-(n//2))))])
#         else:
#             answer += sum(num_list[((n//2)-i):((n//2)+(i+1))])
#     print(f'#{test_case} {answer}')