from collections import deque
import sys

N = int(sys.stdin.readline())

q = deque([])
for i in range(1, N+1):
    q.append(i)

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())
print(q[0])