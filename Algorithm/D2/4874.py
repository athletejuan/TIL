T = int(input())

for test_case in range(1, T+1):
    F = input().split()
    fl = []
    for f in F:
        if f.isdigit():
            fl.append(int(f))
        elif len(fl) > 1:
            b = fl.pop()
            a = fl.pop()
            if f == '+':
                fl.append(a+b)
            elif f == '-':
                fl.append(a-b)
            elif f == '*':
                fl.append(a*b)
            elif f == '/':
                fl.append(a/b)
            else:
                print(f'#{test_case} error')
                break
        elif len(fl) == 1 and f == '.':
            print(f'#{test_case} {int(fl[0])}')
        else:
            print(f'#{test_case} error')
            break