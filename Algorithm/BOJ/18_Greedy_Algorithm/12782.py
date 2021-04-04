T = int(input())

for _ in range(T):
    N,M = input().split()
    N1 = M1 = cnt = 0
    for i in range(len(N)):
        if N[i] == '1':
            N1 += 1
        if M[i] == '1':
            M1 += 1
        if N[i] != M[i]:
            cnt += 1
    if N1 < M1:
        N1,M1 = M1,N1
    print((cnt-N1+M1)//2 + N1-M1)