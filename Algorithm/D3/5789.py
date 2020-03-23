T = int(input())

for test_case in range(1, T+1):
    N, Q = map(int, input().split())
    ranges = []
    new = []
    for i in range(Q):
        ranges.append(list(map(int, input().split())))
    for j in range(1, N+1):
        num = 0
        count = 0
        for k in ranges[::-1]:
            if k[0] <= j <= k[1]:
                num = Q-count
                break
            count += 1
        new.append(str(num))
    print(f'#{test_case} {" ".join(new)}')