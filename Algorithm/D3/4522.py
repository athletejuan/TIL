T = int(input())

for test_case in range(1, T+1):
    pal = input()
    if pal == pal[::-1]:
        print(f'#{test_case} Exist')
    else:
        for i in range(len(pal)):
            if pal[i] == '?' or pal[-(i+1)] == '?':
                continue
            else:
                if pal[i] != pal[-(i+1)]:
                    print(f'#{test_case} Not exist')
                    break
        else:
            print(f'#{test_case} Exist')