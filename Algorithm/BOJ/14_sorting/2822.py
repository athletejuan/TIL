total, top, score = [], [], 0

for i in range(8):
    total.append([i, int(input())])
high_score = sorted(total, key=lambda x: x[1])[3:]
for high in high_score:
    top.append(high[0]+1)
    score += high[1]
print(score)
print(' '.join(map(str, sorted(top))))