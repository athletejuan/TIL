Z = 1
count = [0]*10
for _ in range(3):
    Z *= int(input())
while Z:
    c = Z % 10
    count[c] += 1
    Z //= 10
for i in range(10):
    print(count[i])