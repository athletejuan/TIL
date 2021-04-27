import heapq
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    min_hq, max_hq = [], []
    visited = [0] * 1000000
    k = int(input())
    for i in range(k):
        op, n = input().split()
        if op == 'I':
            heapq.heappush(min_hq, (int(n), i))
            heapq.heappush(max_hq, (-int(n), i))
            visited[i] = 1
        elif n == '1':
            while max_hq and not visited[max_hq[0][1]]:
                heapq.heappop(max_hq)
            if max_hq:
                visited[max_hq[0][1]] = 0
                heapq.heappop(max_hq)
        else:
            while min_hq and not visited[min_hq[0][1]]:
                heapq.heappop(min_hq)
            if min_hq:
                visited[min_hq[0][1]] = 0
                heapq.heappop(min_hq)
    while max_hq and not visited[max_hq[0][1]]:
        heapq.heappop(max_hq)
    while min_hq and not visited[min_hq[0][1]]:
        heapq.heappop(min_hq)
    if max_hq:
        print(-max_hq[0][0], min_hq[0][0])
    else:
        print('EMPTY')