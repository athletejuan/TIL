T = int(input())

for test_case in range(1, T+1):
    N,M = map(int, input().split())
    sum_two = []
    num1 = list(map(int, input().split()))
    num2 = list(map(int, input().split()))
    for i in range(abs(N-M)+1):
        two = 0
        for j in range(i, min(N,M)+i):
            if N < M:
                two += num1[j-i] * num2[j]
            else:
                two += num1[j] * num2[j-i]
        sum_two.append(two)
    print(f'#{test_case} {max(sum_two)}')