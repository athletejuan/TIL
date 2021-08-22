T = int(input())

for tc in range(1, T+1):
    A,B = input().split()

    idx = cnt = 0
    while idx < len(A):
        if A[idx:idx+len(B)] == B:
            idx += len(B)
        else:
            idx += 1
        cnt += 1
    print('#{} {}'.format(tc, cnt))