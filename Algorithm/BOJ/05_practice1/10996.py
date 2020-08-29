N = int(input())

if N == 1:
    print('*')
else:
    for _ in range(N):
        print('* '*((N+1)//2))
        print(' *'*(N//2))