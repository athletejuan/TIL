T = int(input())

for tc in range(1, T+1):
    N = int(input())
    names = [set() for _ in range(50)]
    print('#{}'.format(tc))
    for i in range(N):
        name = input()
        names[len(name)-1].add(name)
    for n in names:
        for j in sorted(n):
            print(j)