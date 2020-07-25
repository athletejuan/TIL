# Practice 1

# 1. 회문 판별

# while
def is_pal_while(word):
    i = 0
    while i < len(word)//2:
        if word[i] != word[-1-i]:
            return False
        i += 1
    return True

print(is_pal_while('tomato'))
print(is_pal_while('racecar'))
print(is_pal_while('azza'))


# recursive
def is_pal_recursive(word):
    if word[0] == word[-1]:
        word = word[1:-1]
        if len(word) < 2:
            return True
        return is_pal_recursive(word)
    else:
        return False

print(is_pal_recursive('tomato'))
print(is_pal_recursive('racecar'))
print(is_pal_recursive('azza'))

# workshop

# 1. 무엇이 중복일까

def duplicated_letters(word):
    dup = set()
    for i in word:
        if word.count(i) > 1:
            dup.add(i)
    return list(dup)

print(duplicated_letters('apple'))
print(duplicated_letters('banana'))

# 2. 소대소대

def low_and_up(word):
    sb = ''
    for idx, char in enumerate(word):
        if idx % 2:
            sb += char.upper()
        else:
            sb += char.lower()
    return sb

print(low_and_up('apple'))
print(low_and_up('banana'))

# 3. 숫자의 의미

def lonely(numbers):
    alone = []
    for num in numbers:
        if not alone or num != alone[-1]:
            alone.append(num)
    return alone

print(lonely([1, 1, 3, 3, 0, 1, 1]))
print(lonely([4, 4, 4, 3, 3]))