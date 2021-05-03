N = int(input())
exam = list(map(int, input().split()))

if exam[0]:
    score = [1]
else:
    score = [0]

for i in range(1, N):
    if not exam[i]:
        score.append(0)
    else:
        score.append(score[i-1] + 1)
print(sum(score))