for tc in range(1, 11):
    N = input()
    eq = input()
    post, stack = [], []
    for i in eq:
        if i.isdecimal():
            post.append(i)
        else:
            if i == '(':
                stack.append(i)
            elif i == '*':
                while stack and stack[-1] == '*':   # 이 조건 없이 stack에 push만 해도 후위표기식 연산결과는 같음
                    post.append(stack.pop())
                stack.append(i)
            elif i == '+':
                while stack and stack[-1] != '(':
                    post.append(stack.pop())
                stack.append(i)
            else:
                while stack and stack[-1] != '(':
                    post.append(stack.pop())
                stack.pop()
    while stack:
        post.append(stack.pop())

    for token in post:
        if token.isdecimal():
            stack.append(token)
        else:
            b = int(stack.pop())
            a = int(stack.pop())
            if token == '+':
                stack.append(a+b)
            else:
                stack.append(a*b)
    print('#{} {}'.format(tc, *stack))

    
# for tc in range(1, 11):
#     N = int(input())
#     # 중위 -> 후위
#     infix = input()
#     stack = []
#     postfix = ''
#     icp = {'*':2, '+':1, '(':3} # in-coming
#     isp = {'*':2, '+':1, '(':0} # in-stack
#     for token in infix:
#         if token.isdigit():
#             postfix += token
#         else:
#             if token == ')':
#                 tmp = ''
#                 while tmp != '(':
#                     postfix += tmp
#                     tmp = stack.pop()
#             elif icp[token] > isp[token]:
#                 stack.append(token)
#             else:
#                 while icp[token] <= isp[stack[-1]]:
#                     postfix += stack.pop()
#                 stack.append(token)
#     stack = []
#     for token in postfix:
#         if token.isdigit():
#             stack.append(token)
#         else:
#             if token == '+':
#                 stack.append(int(stack.pop()) + int(stack.pop()))
#             elif token == '*':
#                 stack.append(int(stack.pop()) * int(stack.pop()))
#
#     print('#{} {}'.format(tc, stack[0]))