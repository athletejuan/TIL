# Workshop

# Faker

# 1.
pip install faker       # faker 라는 외부 패키지를 설치, 파이썬과 pip 가 설치되어있는 쉘 어디서든 가능

# 2.
from faker import Faker # faker package 에서 Faker class를 불러오기 위한 코드이다
fake = Faker()          # Faker는 클래스, fake는 인스턴스
fake.name()             # name()은 fake의 메서드
# 3.
print(fake.name())

fake_ko = Faker('ko_KR')
print(fake_ko.name())

class Faker():
    def __init__(self, locale='en_US'):
        self.locale = locale

# ex1 = Faker()
# ex2 = Faker('ko_KR')
# print(ex1.locale)
# print(ex2.locale)

# 4.
import random
random.random()
random.random()

random.seed(7777)
print(random.random())

random.seed(7777)
print(random.random())

# .seed(class method)
fake = Faker('ko_KR')
Faker.seed(247)             # 김준호
# fake.seed_instance(4321)
print(fake.name())

# .seed_instance(instance method)
fake2 = Faker('ko_KR')
fake2.seed_instance(384)    # 이지영
print(fake2.name())

# homework

# 1. Python 기본 클래스 5개 이상
int, float, complex, str, map, zip, ...and

# 2. 매직 메서드 역할
__init__: 인스턴스가 생성될 때 실행
__del__: 인스턴스가 삭제될 때 실행
__str__: 인스턴스를 print() 할때 보여질 값을 반환
__repr__: 인스턴스 자체가 반환할 값을 반환

# 3. 문자열, 리스트, 딕셔너리 조작하는 메서드 3개 이상
list - .sort(), .append(), .extend(), .count(), ...
str - .upper(), .lower(), .swapcase(), .isalpha(), ...
dict - .get(), .update(), .pop(), ...

# 4. fibo 함수 실행 코드

def fibo_recursion(n):
    if n < 2:
        return n
    else:
        return fibo_recursion(n-1) + fibo_recursion(n-2)

from (a) import (b) as (c)

recursion(4)

(a): fibo
(b): fibo_recursion
(c): recursion


# def my_name(name):
#     i = 0
#     while True:
#         fake = Faker('ko_KR')
#         Faker.seed(i)
#         if fake.name() == name:
#             return i
#         else:
#             print(fake.name())
#             i += 1

# print(my_name(''))