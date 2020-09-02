for test_case in range(1, 11):
    T = input()
    ps = input()
    check = []
    op = '([{<'
    cl = ')]}>'
    for _ in ps:
        if _ in op:
            check.append(_)
        else:
            if op.index(check[-1]) == cl.index(_):
                check.pop()
            else:
                print(f'#{test_case} 0')
                break
    else:
        if not check:
            print(f'#{test_case} 1')
        else:
            print(f'#{test_case} 0')