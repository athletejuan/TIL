import heapq
import sys
input = sys.stdin.readline

N = int(input())
hq = []

for _ in range(N):
    x = int(input())
    if not x:
        print(heapq.heappop(hq)[1] if hq else 0)
    else:
        heapq.heappush(hq, [int((x**2)**.5), x])