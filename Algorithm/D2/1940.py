T = int(input())

for test_case in range(1, T+1):
    number = int(input())
    v = 0
    d = 0
    for i in range(number):
        acc = input()
        num_list = acc.split()
        if num_list[0] == '1':
            v += int(num_list[1])            
        elif num_list[0] == '2':
            v -= int(num_list[1])
            if v < 0:
                v = 0
        d += v
    print(f'#{test_case} {d}')