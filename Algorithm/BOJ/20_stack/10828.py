import sys

N = int(sys.stdin.readline())

s = []
for i in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        s.append(order[1])
    elif order[0] == 'pop':
        if s:
            print(s.pop())
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(s))
    elif order[0] == 'empty':
        if s:
            print(0)
        else:
            print(1)
    elif order[0] == 'top':
        if s:
            print(s[-1])
        else:
            print(-1)