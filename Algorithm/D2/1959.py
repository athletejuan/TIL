T = int(input())

for test_case in range(1, T+1):
    N,M = map(int, input().split())
    num1 = list(map(int, input().split()))
    num2 = list(map(int, input().split()))
    if N < M:
        N,M,num1,num2 = M,N,num2,num1
    for i in range(N-M+1):
        couple = 0
        for j in range(i, i+M):
            couple += num1[j] * num2[j-i]
        if not i:
            max_couple = couple
        elif couple > max_couple:
            max_couple = couple
    print(f'#{test_case} {max_couple}')