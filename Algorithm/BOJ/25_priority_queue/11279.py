import heapq
import sys
input = sys.stdin.readline

N = int(input())
hq = []

for _ in range(N):
    x = int(input())
    if not x:
        if not hq:
            print(0)
        else:
            print(heapq.heappop(hq)[1])
    else:
        heapq.heappush(hq, [-x, x])