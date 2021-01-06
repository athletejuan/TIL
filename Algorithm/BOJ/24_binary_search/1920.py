import sys
N = int(sys.stdin.readline())
Ns = sys.stdin.readline().split()
Ns.sort()
M = int(sys.stdin.readline())
Ms = sys.stdin.readline().split()

for i in range(M):
    left = 0
    right = N-1
    while left <= right:
        mid = (left + right)//2
        if Ms[i] == Ns[mid]:
            print(1)
            break
        elif Ms[i] > Ns[mid]:
            left = mid+1
        else:
            right = mid-1
    else:
        print(0)