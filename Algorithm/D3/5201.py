T = int(input())

for tc in range(1, T+1):
    N,M = map(int, input().split())
    cons = sorted(list(map(int, input().split())), reverse=True)
    trucks = sorted(list(map(int, input().split())))
    total = 0

    while trucks:
        big = trucks.pop()
        for i in range(len(cons)):
            if big >= cons[i]:
                total += cons.pop(i)
                break
    print('#{} {}'.format(tc, total))