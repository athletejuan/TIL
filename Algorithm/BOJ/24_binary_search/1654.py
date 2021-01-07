# import sys
# K,N = map(int, sys.stdin.readline().split())
K,N = map(int, input().split())
Ls = []

for _ in range(K):
    # Ls.append(int(sys.stdin.readline()))
    Ls.append(int(input()))

low = 0
high = max(Ls)
while low <= high:
    mid = (low + high) // 2
    # zero division error
    if not mid:
        break
    each = 0
    for l in Ls:
        each += l // mid
    if each >= N:
        low = mid+1
    else:
        high = mid-1
print(high)