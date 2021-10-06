T = int(input())

def partition(arr, L, R):
    pivot = arr[L]
    i,j = L,R
    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and pivot <= arr[j]:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[L], arr[j] = arr[j], arr[L]
    return j


def quick(arr, L, R):
    if L < R:
        pivot = partition(arr, L, R)
        quick(arr, L, pivot-1)
        quick(arr, pivot+1, R)


for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick(arr, 0, len(arr)-1)
    print('#{} {}'.format(tc, arr[N//2]))


# runtime error
# T = int(input())
#
# def quick(arr):
#     if len(arr) < 2:
#         return arr
#     pivot = arr[len(arr)//2]
#     left, middle, right = [], [], []
#
#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num > pivot:
#             right.append(num)
#         else:
#             middle.append(num)
#     return quick(left) + middle + quick(right)
#
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     print('#{} {}'.format(tc, quick(arr)[N//2]))