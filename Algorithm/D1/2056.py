T = int(input())

for test_case in range(1, T+1):
    number = input()
    temp = [number[:4], number[4:6], number[6:]]
    if 0 < int(temp[1]) < 8:
        if int(temp[1])%2:
            if 0 < int(temp[2]) < 32:
                print(f"#{test_case} {'/'.join(temp)}")
            else:
                print(f"#{test_case} -1")
        elif int(temp[1])==2:
            if 0 < int(temp[2]) < 29:
                print(f"#{test_case} {'/'.join(temp)}")
            else:
                print(f"#{test_case} -1")
        else:
            if 0 < int(temp[2]) < 31:
                print(f"#{test_case} {'/'.join(temp)}")
            else:
                print(f"#{test_case} -1")
    elif 7 < int(temp[1]) < 13:
        if int(temp[1])%2:
            if 0 < int(temp[2]) < 31:
                print(f"#{test_case} {'/'.join(temp)}")
            else:
                print(f"#{test_case} -1")
        else:
            if 0 < int(temp[2]) < 32:
                print(f"#{test_case} {'/'.join(temp)}")
            else:
                print(f"#{test_case} -1")
    else:
        print(f"#{test_case} -1")