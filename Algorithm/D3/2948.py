T = int(input())

for test_case in range(1, T+1):
    num = list(map(int, input().split()))
    s1 = input().split()
    s2 = input().split()
    s3 = set(s1) & set(s2)
    print(f'#{test_case} {len(s3)}')