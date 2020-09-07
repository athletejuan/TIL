N = int(input())

users = []
ages = []
for _ in range(N):
    users.append(input().split())
for user in users:
    if not ages or int(user[0]) not in ages:
        ages.append(int(user[0]))
ages = sorted(ages)
for age in ages:
    for user in users:
        if age == int(user[0]):
            print(str(age) + ' ' + user[1])