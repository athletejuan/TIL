T = int(input())

for tc in range(1, T+1):
    N = int(input())
    bus = [list(map(int, input().split())) for _ in range(N)]
    bus_stop = [0] * 5001
    P = int(input())
    stops = [int(input()) for _ in range(P)]

    print('#{}'.format(tc), end=' ')
    for s,g in bus:
        for i in range(s, g+1):
            bus_stop[i] += 1

    for stop in stops:
        print('{}'.format(bus_stop[stop]), end=' ')
    print()


# 1st try
# T = int(input())
#
# for test_case in range(1, T+1):
#     N = int(input())
#     bus = []
#     for test in range(N):
#         bus.append(list(map(int, input().split())))
#     P = int(input())
#     bus_stop = []
#     for s in range(P):
#         stop = int(input())
#         bus_stop.append(stop)
#     ans = []
#     for i in bus_stop:
#         count = 0
#         for j in bus:
#             if j[0] <= i <= j[1]:
#                 count += 1
#         ans.append(str(count))
#     print(f'#{test_case} {" ".join(ans)}')