num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
S,T = 0, 0

for i in range(4):
    S += num1[i]
    T += num2[i]
S = T if S < T else S
print(S)