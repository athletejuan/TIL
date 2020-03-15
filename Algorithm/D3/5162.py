T = int(input())

for test_case in range(1, T+1):
    A, B, C = map(int, input().split())
    result = C // min(A, B)
    print(f'#{test_case} {result}')