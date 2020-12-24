while True:
    chars = input()
    stack = []
    if chars == '.':
        break
    breaker = True
    for char in chars:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] == '[':
                breaker = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif char == ']':
            if not stack or stack[-1] == '(':
                breaker = False
                break
            elif stack[-1] == '[':
                stack.pop()
    if breaker and not stack:
        print('yes')
    else:
        print('no')