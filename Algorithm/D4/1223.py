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


# lecture code
# for tc in range(1, 11):
#     s1 = []
#     s2 = []

#     # 테스트 케이스 길이
#     N = int(input())
#     # 계산식
#     data = input()

#     """
#     1. 중위표현식 -> 후위표현식 
#     """
#     # 계산식에서 하나씩 값을 가져오면서
#     for c in data:
#         # 숫자면
#         if '0' <= c <= '9':
#             # stack1에 추가
#             s1.append(c)
#         # 연산자면
#         else:
#             # + 연산자면
#             if c == '+':
#                 # stack2가 비워지기 전까지
#                 while len(s2) != 0:
#                     # stack2에서 계속 pop을해서 stack1에 옮기고
#                     s1.append(s2.pop())
#                 # stack2가 다 비워졌다면 해당 연산자를 stack2에 추가하고
#                 s2.append(c)
#             # * 연산자면
#             else:
#                 # 바로 stack2에 추가한다. (+보다 우선순위 위)
#                 s2.append(c)
#     print(s2)
#     # stack2가 비워질 때까지
#     while len(s2) != 0:
#         # s2에서 pop을하고 그걸 stack1으로 옮긴다.
#         s1.append(s2.pop())
#     print(s1)

#     """
#     2. 후위표현식으로 변환된 요소를 실제 계산
#     """
#     # stack1에서 값을 꺼내
#     for c in s1:
#         # 숫자라면
#         if '0' <= c <= '9':
#             # 형변환을 해서 stack2에 넣고
#             s2.append(int(c))
#         # 연산자면
#         else:
#             # s2에서 값을 꺼내고 (2개의 숫자를 연산해야 하기 때문에 2개)
#             opr1 = s2.pop()
#             opr2 = s2.pop()
#             # c가 +면
#             if c == '+':
#                 # 더해서 넣고
#                 s2.append(opr1 + opr2)
#             # *면
#             else:
#                 # 곱해서 넣자
#                 s2.append(opr1 * opr2)

#     result = s2.pop()

#     print('#{} {}'.format(tc, result))



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