N = int(input())
post = input()
num = [int(input()) for _ in range(N)]
stack = []

for char in post:
    if char.isalpha():
        stack.append(num[ord(char)-65])
    else:
        b = stack.pop()
        a = stack.pop()
        if char == '+':
            stack.append(a+b)
        elif char == '-':
            stack.append(a-b)
        elif char == '*':
            stack.append(a*b)
        else:
            stack.append(a/b)
print('{:.2f}'.format(stack[0]))