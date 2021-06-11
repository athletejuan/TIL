N,K = map(int, input().split())

arr = [1, 1]
for i in range(N-1):
    co = [1]
    for i in range(len(arr)-1):
        co.append(arr[i] + arr[i+1])
    arr = co + [1]
print(arr[K]%10007)