T = int(input())

for test_case in range(1, T+1):
    number = input()
    water = number.split()
    a = int(water[0]) * int(water[4])
    if int(water[2]) < int(water[4]):
        ex = int(water[4]) - int(water[2])
        c = int(water[1]) + (ex * int(water[3]))
        if a < int(water[1]) + (ex * int(water[3])):
            print(a)
        else:
            print(int(water[1]) + (ex * int(water[3])))
    else:
        if a < int(water[1]):
            print(a)
        else:
            print(int(water[1]))