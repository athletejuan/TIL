import sys
text = sys.stdin.readline().rstrip()

stack = []

for s in text:
    if s == '(' or s == '[':
        stack.append(s)
    elif s == ')':
        temp = 0

        while stack:
            last = stack.pop()
            if last == '(':
                if temp == 0:
                    stack.append(2)
                else:
                    stack.append(temp*2)
                break
            elif last == '[':
                print(0)
                exit(0)
            else:
                temp += last
    else:
        temp = 0

        while stack:
            last = stack.pop()
            if last == '[':
                if temp == 0:
                    stack.append(3)
                else:
                    stack.append(temp*3)
                break
            elif last == '(':
                print(0)
                exit(0)
            else:
                temp += last

ans = 0
for i in stack:
    if i == "(" or i == "[":
        print(0)
        exit(0)
    else:
        ans += i
print(ans)


# text = input()
# stack = []
# n = 0

# for s in text:
#     if s == '(' or s == '[':
#         stack.append(s)
#     elif s == ')':
#         last = stack.pop()
#         if last == '(':
#             stack.append(2)
#         elif last == '[':
#             print(0)
#             break
#         else:
#             while type(stack[-1]) == int:
#                 last += stack.pop()
#             stack.pop()
#             stack.append(last*2)
#     else:
#         last = stack.pop()
#         if last == '[':
#             stack.append(3)
#         elif last == '(':
#             print(0)
#             break
#         else:
#             while type(stack[-1]) == int:
#                 last += stack.pop()
#             stack.pop()
#             stack.append(last*3)
# else:
#     if type(stack[0]) != int:
#         print(0)
#     else:
#         print(sum(stack))