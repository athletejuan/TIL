def unzip():
    repeat = stack.pop()
    length = 1 if type(repeat) == str else repeat
    if repeat != '(':
        while stack[-1] != '(':
            last = stack.pop()
            if type(last) == str:
                length += 1
            else:
                length += last
        stack.pop()
        stack.append(int(stack.pop())*length)
    else:
        stack.pop()


string = input()
stack, result = [], 0
for s in string:
    if s == ')':
        unzip()
    else:
        stack.append(s)

for i in stack:
    if type(i) == str:
        result += 1
    else:
        result += i
print(result)