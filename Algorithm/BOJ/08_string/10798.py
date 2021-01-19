words = []
longest = 0
column = ''

for _ in range(5):
    row = input()
    words.append(row)
    if len(row) > longest:
        longest = len(row)
for i in range(longest):
    for j in range(5):
        if words[j]:
            column += words[j][0]
            words[j] = words[j][1:]
print(column)