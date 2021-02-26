A1,B1 = map(int, input().split())
A2,B2 = map(int, input().split())

A = A1*B2+A2*B1
B = B1*B2
U = A
D = B

while B:
    if A < B:
        A,B = B,A
    A,B = B,A-B

print(U//A, D//A)