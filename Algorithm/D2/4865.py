T = int(input())

for test_case in range(1, T+1):
    str1 = input()
    str2 = input()

    rank = 0
    for i in str1:
        if str2.count(i) > rank:
            rank = str2.count(i)
    print(f'#{test_case} {rank}')