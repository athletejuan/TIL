T = int(input())

for _ in range(T):
    n = int(input())
    closet = {}
    for i in range(n):
        cloth = input().split()
        if cloth[1] in closet:
            closet[cloth[1]] += 1
        else:
            closet[cloth[1]] = 1
    count = 1
    for case in closet.values():
        count *= (case+1)
    print(count-1)