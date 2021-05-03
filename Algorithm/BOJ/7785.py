n = int(input())
enter = {}

for _ in range(n):
    member = input().split()
    if member[0] not in enter:
        enter[member[0]] = 1
    else:
        enter[member[0]] += 1

attend = []
for name, check in enter.items():
    if check%2:
        attend.append(name)

for i in sorted(attend, reverse=True):
    print(i)