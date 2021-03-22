N = int(input())
scores = [int(input()) for _ in range(N)]
count = 0
check = scores[-1]

for i in range(N-1):
    if scores[N-2-i] > check-1:
        count += scores[N-2-i] - check + 1
        scores[N-2-i] = check-1
    check = scores[N-2-i]
print(count)