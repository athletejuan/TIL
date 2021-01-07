def q4(word):
    ssafy = 'safy'
    for char in word:
        if char in ssafy:
            return True
    return False

print(q4('fish'))
print(q4('united'))
print(q4('galaxy'))