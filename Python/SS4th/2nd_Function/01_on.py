# Workshop

# 1. List의 합 구하기

def list_sum(numbers):
    sum_value = 0
    for number in numbers:
        sum_value += number
    return sum_value

print(list_sum([1, 2, 3, 4, 5]))

# 2. Dictionary로 이루어진 List의 합 구하기

def dict_list_sum(infos):
    age_sum = 0
    for info in infos:
        age_sum += info['age']
    return age_sum

print(dict_list_sum([{'name': 'kim', 'age': 12}, {'name':'lee', 'age':4}]))

# 3. 2차원 List의 전체 합 구하기

def all_list_sum(num_lists):
    lists_sum = 0
    for num_list in num_lists:
        for num in num_list:
            lists_sum += num
    return lists_sum

print(all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]))

# Homework

# 1. Python에서 기본적으로 사용할 수 있는 Built-in Functions 중, 5개를 작성하시오.

dir(__builtins__)
'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip'

# 2. 정중앙 문자

def get_middle_char(word):
    num = len(word) // 2

    if len(word) % 2:
        middle = word[num]
    else:
        middle = word[num-1:num+1]
    return middle

print(get_middle_char('ssafy'))
print(get_middle_char('coding'))

# 3. 다음과 같이 함수가 정의되어 있을 때, 보기 중 오류가 발생하는 코드를 고르시오.
# def ssafy(name, location='서울'):
#     print(f'{name}의 지역은 {location}입니다.')

# 키워드 인자를 사용한 뒤에 위치 인자를 활용할 수는 없습니다.

# 1) ssafy('허준')
# 2) ssafy(location='대전', name='철수')
# 3) ssafy('영희', location='광주')
# 4) ssafy(name='길동', '구미') <-

# 4. 다음과 같이 코드가 작성되어 있을 때, 변수 result에 저장된 값을 작성하시오.
def my_func(a, b):
    c = a + b
    print(c)
    # return c

result = my_func(3, 7)
print(result)

# print는 출력만 할 뿐, 변수에 값을 할당하지 않는다. 변수에 할당하고자 할때는 return 을 써야 한다.

# 5. 가변 인자 리스트를 사용하여, 정수 여러 개를 받아 평균 값을 반환하는 함수 my_avg를 작성하시오.
def my_avg(*arg):
    return sum(arg)/len(arg) 

print(my_avg(77, 83, 95, 80, 70))

# 6. 회문 또는 Palindrome은 거꾸로 읽어도 제대로 읽는 것과 같은 문장이나, 단어를 의미한다. 따라서, ’a’, ‘nan’, ‘토마토’는 모두 Palindrome에 해당한다. 단어를 입력받아 Palindrome을 검증하고 True나 False를 반환하는 함수 palindrome(word)을 작성하시오.

def palindrome(word):
    for i in range(len(word)):
        if word[i] != word[-i-1]:
            return False
    else:
        return True

    return word == word[::-1]
    return list(word) == list(reversed(word))
    return word == ''.join(reversed(word))

print(palindrome('ㅗㅑㅗㅑㅗㅑㅗㅑㅗ'))
print(palindrome('ㅗㅜㅑㅗㅜㅑㅗㅜㅑ'))

