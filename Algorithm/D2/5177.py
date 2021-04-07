T = int(input())

def heap(i):
    while i//2:
        if tree[i//2] > tree[i]:
            tree[i//2],tree[i] = tree[i],tree[i//2]
        i //= 2

for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    nums = list(map(int, input().split()))
    total = 0

    for i in range(N):
        tree[i+1] = nums[i]
        heap(i+1)
        
    while N:
        total += tree[N//2]
        N //= 2
    print('#{} {}'.format(tc, total))