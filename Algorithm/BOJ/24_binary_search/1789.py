S = int(input())

a = 1
while S - a > a:
    S -= a
    a += 1
print(a)