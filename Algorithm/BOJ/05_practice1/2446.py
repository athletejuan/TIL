N = int(input())

b = 0
for i in range(2*N-1, 0, -2):
    print(' '*b+'*'*i)
    b += 1
b -= 1
for j in range(3, 2*N, 2):
    b -= 1
    print(' '*b+'*'*j)