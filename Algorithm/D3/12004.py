T = int(input())

for tc in range(1, T+1):
    N = int(input())
    for i in range(2, 10):
        if N == 1 or not N % i and N//i < 10:
            print('#{} Yes'.format(tc))
            break
    else:
        print('#{} No'.format(tc))
