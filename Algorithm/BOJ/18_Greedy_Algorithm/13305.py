N = int(input())

dist = list(map(int, input().split()))
gas = list(map(int, input().split()))
cheap = gas[0]
refuel = 0
fare = 0

for idx,l in enumerate(gas):
    if cheap > l:
        move = sum(dist[refuel:idx])
        fare += cheap*move
        refuel, cheap = idx, l
print(fare + cheap*sum(dist[refuel:idx]))