T = int(input())

for test_case in range(1, T+1):
    score = list(map(int, input().split()))
    for idx, p in enumerate(score):
        if p < 40:
            score.pop(idx)
            score.insert(idx, 40)
    print(f'#{test_case} {sum(score) // 5}')