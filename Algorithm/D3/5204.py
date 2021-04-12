T = int(input())

def merge(arr):
    global cnt
    if len(arr) > 1:
        mid = len(arr)//2
        left,right = arr[:mid], arr[mid:]
        merge(left)
        merge(right)

        li = ri = i = 0
        while li < len(left) and ri < len(right):
            if left[li] < right[ri]:
                arr[i] = left[li]
                li += 1
            else:
                arr[i] = right[ri]
                ri += 1
            i += 1
        arr[i:] = left[li:] if li != len(left) else right[ri:]
        if left[-1] > right[-1]:
            cnt += 1

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    merge(arr)

    print('#{} {} {}'.format(tc, arr[N//2], cnt))