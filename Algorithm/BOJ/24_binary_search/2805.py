import sys
N,M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
h = sum(trees) - M

low = 0
high = max(trees)
while low <= high:
    mid = (low + high) // 2
    piece = 0
    for t in trees:
        if t < mid:
            piece += t
        else:
            piece += mid
    if h >= piece:
        low = mid+1
    else:
        high = mid-1
else:
    print(high)