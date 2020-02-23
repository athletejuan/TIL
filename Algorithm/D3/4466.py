T = int(input())

for test_case in range(1, T+1):
    num = list(map(int, input().split()))
    score = list(map(int, input().split()))
    print(f'#{test_case} {sum(sorted(score, reverse=True)[:num[1]])}')