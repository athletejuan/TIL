infix = input()
post, stack = '', []

for char in infix:
    if char.isalpha():
        post += char
    else:
        if char == '(':
            stack.append(char)
        elif char == '*' or char == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                post += stack.pop()
            stack.append(char)
        elif char == '+' or char == '-':
            while stack and stack[-1] != '(':
                post += stack.pop()
            stack.append(char)
        else:
            while stack and stack[-1] != '(':
                post += stack.pop()
            stack.pop()
while stack:
    post += stack.pop()
print(post)



# infix = input()
# post, stack = [], []
#
# for char in infix:
#     if char.isalpha():
#         post.append(char)
#     else:
#         if char == '(':
#             stack.append(char)
#         elif char == '*' or char == '/':
#             while stack and (stack[-1] != '*' or stack[-1] != '/'):
#                 post.append(stack.pop())
#             stack.append(char)
#         elif char == '+' or char == '-':
#             while stack and (stack[-1] == '+' or stack[-1] == '-'):
#                 post.append(stack.pop())
#             stack.append(char)
#         else:
#             while stack and stack[-1] != '(':
#                 post.append(stack.pop())
#             stack.pop()
# for i in stack:
#     post.append(i)
# print(post)
#
