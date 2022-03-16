T = int(input())
 
for tc in range(1, T+1):
    N,B = map(int, input().split())
    albas = list(map(int, input().split()))
 
    total = 10000 * N
    for i in range(1 << N):
        temp = 0
        for j in range(N):
            if i & (1 << j):
                temp += albas[j]
        if temp >= B and total > temp:
            total = temp
    print(f'#{tc} {total-B}')