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

def is_pal_while(word):
    while len(word) > 1:
        if word[0] == word[-1]:
            word = word[1:-1]
        else:
            return False
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

def is_pal_recursive(word):
    # 1. 종료조건 선언
    if len(word) <= 1:
        return True
    # 2. 양 끝이 같으면 => 다음 subword를 넣어 함수 호출
    if word[0] == word[-1]:
        return is_pal_recursive(word[1:-1])
    # 2-1. 다르면 => False
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

# homework

# 1. Built-in 함수와 메서드
# sorted()와 .sort()의 차이점
# sorted()는 정렬한 결과를 반환하기 때문에 print로 결과를 볼 수 있다
# .sort()는 원본을 변경하고, 반환값은 없기 때문에 print시 None이 출력된다.

a = [3, 2, 4, 8, 6]
b = [5, 1, 9, 0, 7]
print(sorted(a))
print(b.sort())
print(b)

# 2. .extend()와 .append()
# extend()는 iterable의 각 항목을 추가하고, append는 항목 자체를 원소로 추가한다.
a.extend('string')
print(a)
b.append('string')
print(b)

# 3. 복사가 잘 된건가?
a = [1, 2, 3, 4, 5]
b = a

# shallow copy
a = [1, 2, 3]
b = a[:]
# b = list(a)

b[0] = 5
print(a)

# 2중 list인 경우 list안의 list는 적용되지 않음
a = [1, 2, [1, 2]]
b = a[:]

b[2][0] = 3
print(a)

# deepcopy
import copy

a = [1, 2, [1, 2]]
b = copy.deepcopy(a)

b[2][0] = 3
print(a)
print(b)


# practice 2

# 1. 중복되지 않은 숫자의 합
def sum_of_repeat_number(numbers):
    once = []
    multiple = []
    for number in numbers:
        if number in once:
            multiple.append(number)
            once.remove(number)
        elif number not in multiple:
            once.append(number)
    return sum(once)

def sum_of_repeat_number(numbers):
    solo = 0
    for number in numbers:
        if numbers.count(number) == 1:
            solo += number
    return solo

print(sum_of_repeat_number([4, 4, 7, 8, 10]))

# 2. 썩은 과일 찾기
def change_rotten_fruit(fruit_bag):
    fine = []
    for fruit in fruit_bag:
        if fruit[:6] == 'rotten':
            fine.append(fruit[6:].lower())
        else:
            fine.append(fruit)
    return fine

print(change_rotten_fruit(['apple', 'rottenBanana', 'apple']))
print(change_rotten_fruit(['rottenapple', 'rottenBanana', 'apple', 'rottenGrape']))