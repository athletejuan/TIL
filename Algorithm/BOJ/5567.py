n = int(input())
m = int(input())
invited = set()
friends = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

for friend in friends[1]:
    invited.add(friend)
    for f in friends[friend]:
        if f != 1:
            invited.add(f)
print(len(invited))