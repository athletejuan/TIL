count = 0
for i in range(8):
    row = list(input())
    for idx,j in enumerate(row):
        if j == 'F':
            if i%2 and idx%2:
                count += 1
            if not i%2 and not idx%2:
                count += 1
print(count)