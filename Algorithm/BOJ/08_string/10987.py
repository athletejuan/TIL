word = input()
count = 0

for w in word:
    if w in 'aeiou':
        count += 1
print(count)