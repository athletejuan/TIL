N,K = map(int, input().split())
rankers = {}

for i in range(N):
    country = list(map(int, input().split()))
    name = country[0]
    medal = country[1]*(1000000**2)+country[2]*1000000+country[3]
    if name == K:
        check = medal
    for ranker in rankers:
        if ranker == medal:
            rankers[ranker].append(name)
            break
    else:
        rankers[medal] = [name]

rank = 1
for i in sorted(rankers, reverse=True):
    if i != check:
        rank += len(rankers[i])
    else:
        break
print(rank)