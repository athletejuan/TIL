A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

X = A*P
Y = B+(P-C)*D if C < P else B
M = X if X < Y else Y
print(M)