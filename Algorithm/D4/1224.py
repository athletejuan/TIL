for tc in range(1, 11):
    l = int(input())
    eq = input()
    post = ''
    cal = ''
    stack = []
    paren = [0]
    for i in range(l):
        if eq[i] == '(':
            paren.append(len(cal))
        elif eq[i].isdecimal():
            post += eq[i]
        elif eq[i] == '*':
            cal += '*'
        elif eq[i] == '+':
            post += cal[paren[-1]:][::-1]
            cal = cal[:paren[-1]]
            cal += '+'
        else:
            post += cal[paren[-1]:][::-1]
            cal = cal[:paren[-1]]
            paren.pop()
    post += cal
    for p in post:
        if p.isdecimal():
            stack.append(int(p))
        elif p == '+':
            stack.append(stack.pop()+stack.pop())
        else:
            stack.append(stack.pop()*stack.pop())
    print(f'#{tc} {"".join(str(stack[0]))}')


    # for tc in range(1, 11):
    # N = int(input())
    # # 중위 -> 후위
    # infix = input()
    # stack = []
    # postfix = ''
    # icp = {'*':2, '+':1, '(':3} # in-coming
    # isp = {'*':2, '+':1, '(':0} # in-stack
    # for token in infix:
    #     if token.isdigit():
    #         postfix += token
    #     else:
    #         if token == ')':
    #             tmp = ''
    #             while tmp != '(':
    #                 postfix += tmp
    #                 tmp = stack.pop()
    #         elif icp[token] > isp[token]:
    #             stack.append(token)
    #         else:
    #             while icp[token] <= isp[stack[-1]]:
    #                 postfix += stack.pop()
    #             stack.append(token)
    # stack = []
    # for token in postfix:
    #     if token.isdigit():
    #         stack.append(token)
    #     else:
    #         if token == '+':
    #             stack.append(int(stack.pop()) + int(stack.pop()))
    #         elif token == '*':
    #             stack.append(int(stack.pop()) * int(stack.pop()))

    # print('#{} {}'.format(tc, stack[0]))