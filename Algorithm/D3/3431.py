T = int(input())

for test_case in range(1, T+1):
    ex = list(map(int, input().split()))
    if ex[2] < ex[0]:
        print(f'#{test_case} {ex[0]-ex[2]}')
    elif ex[2] > ex[1]:
        print(f'#{test_case} -1')
    else:
        print(f'#{test_case} 0')

    exercise