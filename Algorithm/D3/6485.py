T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    bus = []
    for test in range(N):
        bus.append(list(map(int, input().split())))
    P = int(input())
    bus_stop = []
    for s in range(P):
        stop = int(input())
        bus_stop.append(stop)
    ans = []
    for i in bus_stop:
        count = 0
        for j in bus:
            if j[0] <= i <= j[1]:
                count += 1
        ans.append(str(count))
    print(f'#{test_case} {" ".join(ans)}')