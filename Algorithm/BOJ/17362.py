n = int(input())
finger = n%8

if finger == 1:
    print(1)
elif not finger or finger == 2:
    print(2)
elif finger == 3 or finger == 7:
    print(3)
elif finger == 4 or finger == 6:
    print(4)
else:
    print(5)