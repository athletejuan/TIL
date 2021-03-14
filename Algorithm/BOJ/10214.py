T = int(input())

for tc in range(T):
    Y = 0
    K = 0
    for _ in range(9):
        score = list(map(int, input().split()))
        Y += score[0]
        K += score[1]
    if Y > K:
        print('Yonsei')
    elif Y < K:
        print('Korea')
    else:
        print('Draw')