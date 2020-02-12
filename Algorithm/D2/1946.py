T = int(input())

for test_case in range(1, T+1):
    number = int(input())
    alpha_list = []
    for i in range(number):
        z = input().split()
        for j in range(int(z[1])):
            alpha_list.append(z[0])
    answer = ''
    for idx, value in enumerate(alpha_list):
        answer += value
        if (idx+1) % 10 == 0:
            answer += '\n'
    print(f'#{test_case}')
    print(''.join(answer))