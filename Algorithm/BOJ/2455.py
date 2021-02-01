start = input().split()
max_num = int(start[1])
now = int(start[1])

for i in range(2):
    station = list(map(int, input().split()))
    now += station[1] - station[0]
    if now > max_num:
        max_num = now
fin = input()
print(max_num)