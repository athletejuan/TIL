T = int(input())

for tc in range(1, T+1):
    text = input()
    stack = []

    for i in text:
        if i == '(' or i == '{':
            stack.append(i)
        # 닫힌 괄호가 나온 경우라면 stack이 비어있으면 안된다(SWEA Runtime error)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
        elif i == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(i)

    result = 0 if stack else 1
    print('#{} {}'.format(tc, result))