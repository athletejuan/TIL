T = int(input())

def binary_search():
    global A, cnt
    left,right = 0,N-1
    before = None
    while left <= right:
        mid = (left+right)//2
        if i == A[mid]:
            cnt += 1
            return
        elif i < A[mid]:
            right = mid-1
            now = 'L'
        else:
            left = mid+1
            now = 'R'
        if now == before:
            return
        before = now

for tc in range(1, T+1):
    N,M = map(int, input().split())
    cnt = 0
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    for i in B:
        binary_search()
    print('#{} {}'.format(tc, cnt))