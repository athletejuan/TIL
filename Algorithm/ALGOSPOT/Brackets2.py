C = int(input())
op = '({['
cl = ')}]'

for _ in range(C):
    s = []
    ps = input()
    for i in ps:
        if i in op:
            s.append(i)
        else:
            if not s:
                print('NO')
                break
            if op.index(s[-1]) == cl.index(i):
                s.pop()
            else:
                print('NO')
                break
    else:
        if s:
            print('NO')
        else:
            print('YES')