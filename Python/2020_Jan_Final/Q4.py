def q4(word):
    count = {}
    for i in word:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
    return count

print(q4('hello'))
print(q4('internationalization'))
print(q4('haha'))