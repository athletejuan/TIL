def q2(word):
    vowels = 'aeiou'
    count = 0
    for i in word:
        if i in vowels:
            count += 1
    return count

print(q2('hello'))
print(q2('internationalization'))
print(q2('ssafy'))