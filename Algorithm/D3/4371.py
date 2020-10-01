T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    S = input()
    gap = []
    count = 0
    for n in range(N-1):
        gap.append(int(input())-1)
    c = gap[:]
    while gap:
        for i in gap:
            if not i % gap[0]:
                c.remove(i)
        gap = c[:]
        count += 1
    print(f'#{test_case} {count}')
