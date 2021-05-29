A,P = map(int, input().split())
arr, num = [A], 0

while True:
    while A:
        num += (A%10)**P
        A //= 10
    if num not in arr:
        arr.append(num)
        A, num = num, 0
    else:
        print(arr.index(num))
        break