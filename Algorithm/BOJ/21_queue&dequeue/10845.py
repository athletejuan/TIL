from collections import deque
import sys

N = int(sys.stdin.readline())
queue = deque()
for _ in range(N):
    order = sys.stdin.readline().split()
    if len(order) > 1:
        queue.append(order[1])
    if queue:
        if order[0] == 'front':
            print(queue[0])
        elif order[0] == 'back':
            print(queue[-1])
        elif order[0] == 'empty':
            print(0)
        elif order[0] == 'pop':
            print(queue.popleft())
    else:
        if order[0] == 'front' or order[0] == 'back' or order[0] == 'pop':
            print(-1)
        if order[0] == 'empty':
            print(1)
    if order[0] == 'size':
        print(len(queue))