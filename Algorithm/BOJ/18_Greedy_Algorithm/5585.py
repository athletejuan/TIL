Y = 1000 - int(input())

c = 0
while Y:
    T = Y % 10
    c += T//5
    c += T%5
    Y //= 10
print(c)