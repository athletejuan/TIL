for tc in range(1, 11):
    l = int(input())
    eq = input()
    post = eq[0] + eq[2]
    cal = eq[1]
    stack = []
    for i in range(3, l):
        if i%2:
            if eq[i] == '+':
                post += cal[::-1]
                cal = '+'
            else:
                cal += '*'
        else:
            post += eq[i]
    post += cal[::-1]
    for p in post:
        if p.isdecimal():
            stack.append(int(p))
        elif p == '+':
            stack.append(stack.pop()+stack.pop())
        else:
            stack.append(stack.pop()*stack.pop())
    print(f'#{tc} {"".join(str(stack[0]))}')