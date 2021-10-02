T = int(input())

def select_sort(arr):
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


for tc in range(1, T+1):
    N = int(input()) 
    arr = list(map(int, input().split()))
    print('#{}'.format(tc), end=' ')
    print(*select_sort(arr))