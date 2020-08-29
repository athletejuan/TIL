N = int(input())

scores = sorted(list(map(int, input().split())))
total = 0
for _ in range(N):
    total += (scores[_]/scores[-1]*100)
print(total/N)