T = int(input())

for test_case in range(1, T+1):
    date = list(map(int, input().split()))
    cal = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    day = 1
    for i in range(date[0], date[2]+1):
        if i == date[0]:
            day += cal[i] - date[1]
        elif i == date[2]:
            day += date[3]
        else:
            day += cal[i]
    print(f'#{test_case} {day}')