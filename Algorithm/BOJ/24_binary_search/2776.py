T = int(input())

for tc in range(T):
    N = int(input())
    real = list(map(int, input().split()))
    real.sort()
    M = int(input())
    memo = list(map(int, input().split()))

    def binary(L,R,real,memo):
        while L <= R:
            mid = (L+R)//2
            if memo[i] == real[mid]:
                return 1
            elif memo[i] < real[mid]:
                R = mid-1
            else:
                L = mid+1
        else:
            return 0

    for i in range(M):
        A = 0
        B = N-1
        print(binary(A,B,real,memo))