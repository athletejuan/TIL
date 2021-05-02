D,K = map(int, input().split())

def tiger(D,K):
    A,B = 1,1
    while True:
        while A+B <= K:
            a,b = A,B
            for i in range(D-2):
                a,b = b,a+b
                if b > K:
                    break
            else:
                if b == K:
                    print(A)
                    print(B)
                    return
            B += 1
        A += 1
        B = A

tiger(D,K)