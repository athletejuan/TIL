eq = input().split('-')
f = 0
b = 0

for i in range(len(eq)):
    if not i:
        for j in eq[i].split('+'):
            f += int(j)
    else:
        for k in eq[i].split('+'):
            b += int(k)
print(f-b)

# - 가 없는 경우 ft NameError
# for i in range(len(eq)):
#     if eq[i] == '-':
#         f = 0
#         ft = 0
#         b = 0
#         bt = 0
#         for j in eq[:i]:
#             if j.isnumeric():
#                 if not f:
#                     f += int(j)
#                 else:
#                     f *= 10
#                     f += int(j)
#             else:
#                 ft += f
#                 f = 0
#         ft += f
#         for k in eq[i:]:
#             if k.isnumeric():
#                 if not b:
#                     b += int(k)
#                 else:
#                     b *= 10
#                     b += int(k)
#             else:
#                 bt += b
#                 b = 0
#         bt += b
#         print(ft-bt)
#         break