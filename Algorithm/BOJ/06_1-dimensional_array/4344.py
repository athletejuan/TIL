C = int(input())

for _ in range(C):
    scores = list(map(int, input().split()))
    ave = sum(scores[1:])/len(scores[1:])
    good = 0
    for i in scores[1:]:
        if i > ave:
            good += 1
    print(format((good/len(scores[1:])), "5.3%"))