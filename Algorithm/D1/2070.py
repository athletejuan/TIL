T = int(input())

for test_case in range(1, T+1):
    number = input()
    vs = number.split()
    if int(vs[0]) > int(vs[1]):
        print(f'#{test_case} >')
    elif int(vs[0]) < int(vs[1]):
        print(f'#{test_case} <')
    else:
        print(f'#{test_case} =')