N,M = map(int, input().split())
nolisten = []
unknown = []
c = 0

for _ in range(N):
    nolisten.append(input())
nolisten.sort()

for i in range(M):
    nosee = input()
    # Binary Search
    left = 0
    right = N-1
    while left <= right:
        mid = (left + right)//2
        if  nolisten[mid] == nosee:
            unknown.append(nosee)
            c += 1
            break
        elif nolisten[mid] > nosee:
            right = mid-1
        else:
            left = mid+1

unknown.sort()
print(c)
for who in unknown:
    print(who)