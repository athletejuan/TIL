X = int(input())
bi = []

while X:
    bi.append(X%2)
    X //= 2
print(bi.count(1))