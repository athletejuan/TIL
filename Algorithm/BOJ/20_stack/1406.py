import sys

left = list(sys.stdin.readline().strip())
right = []
M = int(sys.stdin.readline().strip())

for _ in range(M):
    c = sys.stdin.readline().split()
    if c[0] == 'P':
        left.append(c[1])
    elif c[0] == 'L' and left:
        right.append(left.pop())
    elif c[0] == 'D' and right:
        left.append(right.pop())    # pop(0)은 시간초과, pop하고 뒤집어서 출력
    elif c[0] == 'B' and left:
        left.pop()
print(''.join(left+right[::-1]))

# left = sys.stdin.readline().strip()
# right = ''
# M = int(sys.stdin.readline().strip())

# for _ in range(M):
#     c = sys.stdin.readline().split()
#     if c[0] == 'P':
#         left = left + c[1]
#     elif c[0] == 'L' and left:
#         right = left[-1] + right
#         left = left[:-1]
#     elif c[0] == 'D' and right:
#         left += right[0]
#         right = right[1:]
#     elif c[0] == 'B' and left:
#         left = left[:-1]
# print(left+right)