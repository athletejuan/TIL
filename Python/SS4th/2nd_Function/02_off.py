# Practice

# 1. abs() 직접 구현하기
def my_abs(x):
    if type(x) == complex:
        return (x.imag**2 + x.real**2) ** (1/2)
    else:
        if x == 0:
            return x ** 2
        if x < 0:
            return x * -1
        else:
            return x
        # return (x ** 2) ** .5

print(my_abs(3+4j))
print(my_abs(-0.0))
print(my_abs(-5))
print(abs(3+4j), abs(-0.0), abs(-5))

# 2. all() 직접 구현하기

def my_all(elements):
    result = True
    for element in elements:
        if not element:
            result = False
            break
    return result

def my_all(elements):
    for element in elements:
        if not element:
            return False
    return True

print(my_all([]))
print(my_all([1, 2, 5, '6']))
print(my_all([[], 2, 5, '6']))
print(all([]), all([1, 2, 5, '6']), all([[], 2, 5, '6']))

# 3. any() 직접 구현하기

def my_any(elements):
    for element in elements:
        if element:
            return True
    return False

print(my_any([1, 2, 5, '6']))
print(my_any([[], 2, 5, '6']))
print(my_any([0]))
print(any([1, 2, 5, '6']), any([[], 2, 5, '6']), any([0]))

# Workshop

# 1. 숫자의 의미

def get_secret_word(numbers):
    word = ''
    for number in numbers:
        word += chr(number)
    return word
print(get_secret_word([83, 115, 65, 102, 89]))

# 2. 나만의 숫자 만들기

def get_secret_number(word):
    total = 0

    for char in word:
        total += ord(char)
    return total
print(get_secret_number('juan'))

# 3. 강한 이름

def get_strong_word(word1, word2):
    word1_total = 0
    word2_total = 0

    for char in word1:
        word1_total += ord(char)
    for char in word2:
        word2_total += ord(char)
    
    if word1_total > word2_total:
        return word1
    else:
        return word2
print(get_strong_word('tom', 'john'))

# 3-1. 2번 문제 함수 활용

def get_strong_word2(word1, word2):
    word1_total = get_secret_number(word1)
    word2_total = get_secret_number(word2)
    
    if word1_total > word2_total:
        return word1
    else:
        return word2
print(get_strong_word2('coding', 'ssafy'))

# Homework

# 1. Python에서 변수를 찾을 때 접근하는 이름 공간을 순서대로 작성하시오.

    Local scope
    Enclosed scope
    Global scope
    Built-in scope

# 2. 다음 중, 옳지 않은 것을 고르시오.
    1) 함수는 오직 하나의 객체만 반환할 수 있으므로, 'return a, b'와 같이 쓸 수 없다. <- return a, b 사용가능, 2개를 리턴하는 것처럼 보이지만 실제로는 (a, b)라는 하나의 튜플 객체를 리턴
    2) 함수에서 return을 작성하지 않으면 None 값을 반환한다.
    3) 함수의 매개변수(parameter)는 함수를 선언할 때 설정한 값이며, 전달 인자(argument)는 함수를 호출할 때 넘겨주는 값이다.
    4) 가변 인자를 설정할 때는 인자 앞에 *를 붙이고, 이 때는 함수 내에서 tuple로 처리된다.

# 3. 재귀 함수를 사용할 때 얻을 수 있는 장점과 단점을 각각 작성하시오.
    # 장점
    # 자기 자신을 호출하는 재귀함수는 알고리즘 구현시 많이 사용된다.
    # 코드가 더 직관적이고 이해하기 쉬운 경우가 있음. (하지만, 만들기는 어려움)
    # 단점
    # Python Tutor에 보면, 함수가 호출될 때마다 메모리 공간에 쌓이는 것을 볼 수 있다.
    # 이 경우, 메모리 스택이 넘치거나(Stack overflow) 프로그램 실행 속도가 늘어지는 단점이 생긴다.
    # 파이썬에서는 이를 방지하기 위해 3,000번이 넘어가게 되면 더이상 함수를 호출하지 않고, 종료된다

# 4. 회문 판별 (extra)
def is_pal_recursive(word):
    word_len = len(word)

    if word_len <= 1:
        return True
    if word[0] == word[-1]:
        return is_pal_recursive(word[1:-1])
    else:
        return False

print(is_pal_recursive('ssafy'))
print(is_pal_recursive('racecar'))

# 5. Python의 sqrt() 함수는 제곱근의 근사값을 반환하는 함수이다.
import math
print('math.sqrt:\t', math.sqrt(2)) # 1.4142135623730951
    # 다음 지문을 참고하여, 양의 정수 x를 입력받아 제곱근의 근사값을 반환하는 함수 my_sqrt()를 작성하시오.

def my_sqrt(n):
    x, y = 1, n
    result = 1

    while abs(result**2 - n) > 0.0000000001:
        result = (x+y)/2
        if result**2 < n:
            x = result
        else:
            y = result
    return result

print('my_sqrt:\t', my_sqrt(2))