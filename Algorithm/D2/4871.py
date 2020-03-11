T = int(input())

for test_case in range(1, T+1):
    V, E = map(int, input().split())
    M = []
    for _ in range(E):
        M.append(list(map(int, input().split())))
    S, G = map(int, input().split())
    con = []
    while S != G:
        for m in M:
            if S == m[0]:
                con.append(m[1])
        if con:
            S = con.pop()
        else:
            print(f'#{test_case} 0')
            break
    else:
        print(f'#{test_case} 1')