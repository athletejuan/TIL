N = int(input())

s = 1
b = 1
while s < N:
    s += 6*b
    b += 1
print(b)