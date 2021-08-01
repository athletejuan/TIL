TC = int(input())

for tc in range(1, TC+1):
    A,B = map(int, input().split())
    if A > 9 or B > 9:
        print('#{} -1'.format(tc))
    else:
        print('#{} {}'.format(tc, A*B))