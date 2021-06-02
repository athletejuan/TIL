word = input()
ex = ''

for c in word:
    if ord(c) > 96:
        ex += chr(ord(c) - 32)
    else:
        ex += chr(ord(c) + 32)
print(ex)