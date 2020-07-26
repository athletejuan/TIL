T = int(input())

for test_case in range(1, T+1):
    time = list(map(int, input().split()))
    h = 0
    m = 0
    for idx, t in enumerate(time):
        if idx % 2:
            m += t
            if m > 60:
                m -= 60
                h += 1
        else:
            h += t
    if h > 12:
        h -= 12
    print(f'#{test_case} {h} {m}')