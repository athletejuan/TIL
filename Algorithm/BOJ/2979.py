A,B,C = map(int, input().split())
parking = [0] * 101
for _ in range(3):
    i,o = map(int, input().split())
    for j in range(i, o):
        parking[j] += 1

fee = 0
for k in range(1, 101):
    if parking[k] == 1:
        fee += A
    elif parking[k] == 2:
        fee += (2*B)
    elif parking[k] == 3:
        fee += (3*C)
print(fee)