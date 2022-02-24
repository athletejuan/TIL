T = int(input())

def Forth():
    for f in post:
        if f.isdecimal():
            stack.append(int(f))
        elif len(stack) > 1:
            b = stack.pop()
            a = stack.pop()
            if f == '+':
                stack.append(a+b)
            elif f == '-':
                stack.append(a-b)
            elif f == '*':
                stack.append(a*b)
            elif f == '/':
                stack.append(a//b)
            else:
                return 'error'
        elif stack and f == '.':
            return stack[0]
        else:
            return 'error'

for tc in range(1, T+1):
    post = input().split()
    stack = []
    print('#{} {}'.format(tc, Forth()))
    # for f in post:
    #     if f.isdigit():
    #         stack.append(int(f))
    #     elif len(stack) > 1:
    #         b = stack.pop()
    #         a = stack.pop()
    #         if f == '+':
    #             stack.append(a+b)
    #         elif f == '-':
    #             stack.append(a-b)
    #         elif f == '*':
    #             stack.append(a*b)
    #         elif f == '/':
    #             stack.append(a/b)
    #         else:
    #             print(f'#{tc} error')
    #             break
    #     elif len(stack) == 1 and f == '.':
    #         print(f'#{tc} {int(stack[0])}')
    #     else:
    #         print(f'#{tc} error')
    #         break