# Workshop

# 1. 평균점수 구하기

def get_dict_avg(scores):
    score_sum = 0
    for value in scores.values():
        score_sum += value
    average = score_sum / len(scores)
    return average

print(get_dict_avg({'python': 80, 'algorithm': 90, 'django': 89, 'web': 83}))

# 2. 혈액형 분류하기

def count_blood(bloods):
    blood_type = {}
    blood_type['A'] = bloods.count('A')
    blood_type['B'] = bloods.count('B')
    blood_type['O'] = bloods.count('O')
    blood_type['AB'] = bloods.count('AB')
    return blood_type

print(count_blood(['A','B','A','O','AB','AB','O','A','B','O','B','AB']))

# Homework

# 1. 모음은 몇 개나 있을까?

def count_vowels(word):
    count = 0
    for char in word:
        if char in 'aeiou':
            count += 1
    return count

print(count_vowels('apple'))
print(count_vowels('banana'))

# 2. 문자열 조작

(1) .find(x)는 x의 첫 번째 위치를 반환한다. 없으면 -1을 반환한다.
(2) .split([chars])은 특정 문자를 지정하면 문자열을 특정 문자를 기준으로 나누어 list로 반환한다. 특정 문자를 지정하지 않으면 공백을 기준으로 나눈다.
(3) .replace(old, new[, count])는 바꿀 대상 문자를 새로운 문자로 바꿔서 반환한다.
(4) .strip([chars])은 특정 문자를 지정하면, 양쪽에서 해당 문자를 찾아 제거한다. 특정 문자를 지정하지 않으면 오류가 발생한다. <- 문자 양쪽 공백 제거

# 3. 정사각형만 만들기

def only_square_area(list1, list2):
    square = []
    for length in list1:
        if length in list2:
            square.append(length**2)
    return square

print(only_square_area([32, 55, 63], [13, 32, 40, 55]))