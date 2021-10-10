N = int(input())
chicken = list(map(int, input().split()))
k = int(input())

def taste(chicken, N, k):
    if k == 1:
        print(*sorted(chicken), end=' ')
        return
    taste(chicken[:N//2], N//2, k//2)
    taste(chicken[N//2:], N//2, k//2)

taste(chicken, N, k)