from collections import deque
import sys

N = int(sys.stdin.readline())
deq = deque()

for _ in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'push_back':
        deq.append(order[1])
    elif order[0] == 'push_front':
        deq.appendleft(order[1])
    elif order[0] == 'size':
        print(len(deq))
    if deq:
        if order[0] == 'pop_front':
            print(deq.popleft())
        elif order[0] == 'pop_back':
            print(deq.pop())
        elif order[0] == 'front':
            print(deq[0])
        elif order[0] == 'back':
            print(deq[-1])
        elif order[0] == 'empty':
            print(0)
    else:
        if order[0] in ['pop_front', 'pop_back', 'front', 'back']:
            print(-1)
        elif order[0] == 'empty':
            print(1)        