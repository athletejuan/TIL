for tc in range(1, 11):
    N = int(input())
    eq = list(input())
    stack, post = [], []
    for i in eq:
        if i.isdecimal():
            post.append(int(i))
        else:
            if i == '+':
                while stack:
                    post.append(stack.pop())
                stack.append(i)
            else:
                while stack and stack[-1] == '*':
                    post.append(stack.pop())
                stack.append(i)
    while stack:
        post.append(stack.pop())

    for i in post:
        if i == '+':
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num1 + num2)
        elif i == '*':
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num1 * num2)
        else:
            stack.append(i)

    result = stack[0]
    print('#{} {}'.format(tc, result))


# 1st try
# for tc in range(1, 11):
#     l = int(input())
#     eq = input()
#     post = eq[0] + eq[2]
#     cal = eq[1]
#     stack = []
#     for i in range(3, l):
#         if i%2:
#             if eq[i] == '+':
#                 post += cal[::-1]
#                 cal = '+'
#             else:
#                 cal += '*'
#         else:
#             post += eq[i]
#     post += cal[::-1]
#     for p in post:
#         if p.isdecimal():
#             stack.append(int(p))
#         elif p == '+':
#             stack.append(stack.pop()+stack.pop())
#         else:
#             stack.append(stack.pop()*stack.pop())
#     print(f'#{tc} {"".join(str(stack[0]))}')