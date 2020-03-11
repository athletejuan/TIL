T = int(input())

for test_case in range(1, T+1):
    text = input()
    op = '({'
    cl = ')}'
    ol = []
    for i in text:
        if i in op:
            ol.append(i)
        elif i in cl:
            if ol and op.index(ol[-1]) == cl.index(i):
                ol.pop()
            else:
                print(f'#{test_case} 0')
                break
    else:
        if ol:
            print(f'#{test_case} 0')
        else:
            print(f'#{test_case} 1')