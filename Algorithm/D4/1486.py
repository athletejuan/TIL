T = int(input())

for test_case in range(1, T+1):
    N,B = map(int, input().split())
    albas = list(map(int, input().split()))

    total = []
    for i in range(1 << N):
        sub_alba = []
        for j in range(N):
            if i & (1 << j):
                sub_alba.append(albas[j])
        if sum(sub_alba) >= B:
            total.append(sum(sub_alba))
    print(f'#{test_case} {min(total)-B}')