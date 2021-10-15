T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    visited = [0] * N
    cnt = 0

    for i in range(N):
        idx = i
        if not visited[idx]:
            while not visited[arr[idx]-1]:
                visited[arr[idx]-1] = 1
                idx = arr[idx]-1
            cnt += 1
    print(cnt)