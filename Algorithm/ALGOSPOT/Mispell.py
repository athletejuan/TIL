N = int(input())

for t in range(1,N+1):
    M = input().split()
    print('{} {}'.format(t, M[1][:(int(M[0])-1)]+M[1][int(M[0]):]))