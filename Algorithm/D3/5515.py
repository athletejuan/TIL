T = int(input())

for test_case in range(1, T+1):
    m, d = map(int, input().split())
    if m == 1:
        days = 0
    elif m < 6:
        if m == 3:
            days = 60
        else:
            days = 30 * (m-1) + 1
    elif m < 8:
        days = 30 * (m-1) + 2
    elif m < 9:
        days = 30 * (m-1) + 3
    elif m < 11:
        days = 30 * (m-1) + 4
    else:
        days = 30 * (m-1) + 5
    day = (((days + d) % 7 + 3) % 7)
    print(f'#{test_case} {day}')