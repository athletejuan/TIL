import sys
input = sys.stdin.readline
stack = []
start = input()

while True:
    debug = input()
    if len(debug) > 5:
        break
    if len(debug) < 4:
        stack.append('problem')
    else:
        if not stack:
            stack.extend(['problem', 'problem'])
        else:
            stack.pop()
if not stack:
    print('고무오리야 사랑해')
else:
    print('힝구')


# 1st try
# problem = 0
# start = input()

# while True:
#     debug = input()
#     if len(debug) > 5:
#         break
#     if len(debug) < 4:
#         problem += 1
#     else:
#         if not problem:
#             problem += 2
#         else:
#             problem -= 1
# if not problem:
#     print('고무오리야 사랑해')
# else:
#     print('힝구')