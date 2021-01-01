s = input()
stack = []
n = 0

for i in s:
    if i == '(':
        stack.append(i)
        l = ''
    else:
        if l:
            l = stack.pop()
            n += 1
        else:
            l = stack.pop()
            n += len(stack)
print(n)