import pprint
# Practice 1

# 1.

class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0
    
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1
        
    def __del__(self):
        Doggy.num_of_dogs -= 1
    
    def bark(self):
        return '왈왈!'
    
    @classmethod
    def get_status(cls):
        return f'Birth: {cls.birth_of_dogs}, Current: {cls.num_of_dogs}'


d1 = Doggy('초코', '푸들')
d2 = Doggy('꽁이', '말티즈')
d3 = Doggy('별이', '시츄')

print(d1.bark())
print(d2.bark())
print(d3.bark())

# d3 = 'byebye'
# del(d2)

# print(d1.name)
# # print(d2)
# print(d3)

print(Doggy.get_status())

# Workshop

# 1.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, p1, p2):
        width = abs(p1.x - p2.x)
        height = abs(p1.y - p2.y)
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
    def is_square(self):
        if self.width == self.height:
            return True
        return False

p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())
p3 = Point(3, 7)
p4 = Point(6, 5)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())

# homework

# 1.
class Circle:
    pi = 3.14
    x = 0
    y = 0
    r = 0

    def __init__(self):
        self.r = Circle.r
        self.x = Circle.x
        self.y = Circle.y

    def area(self):
        return self.pi * self.r ** 2

    def circumference(self):
        return 2 * self.pi * self.r

    def center(self):
        return (self.x, self.y)

c1 = Circle()
print(c1.area())
print(c1.circumference())
print(c1.center())

# 2.
class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f'{self.name}! 걷는다!')

    def eat(self):
        print(f'{self.name}! 먹는다!')

class Dog(Animal):
    def walk(self):
        print(f'{self.name}! 달린다!')

    def bark(self):
        print(f'{self.name}! 짖는다!')

class Bird(Animal):
    def fly(self):
        print(f'{self.name}! 푸드덕!')

dog = Dog('멍멍이')
dog.walk() # 멍멍이! 달린다!
dog.bark() # 멍멍이! 짖는다!

bird = Bird('구구')
bird.walk() # 구구! 걷는다!
bird.eat() # 구구! 먹는다!
bird.fly() # 구구! 푸드덕!

# 3.
ZeroDivisionError # 0으로 나누려고 할 때
NameError # 정의 되지 않은 변수 사용
TypeError # 자료형에 대한 잘못된 사용
IndexError # Index 범위를 벗어나서 참조하려 할 때
KeyError # Dict에 없는 Key를 찾으려 할 때
ModuleNotFoundError # 모듈을 찾을 수 없는 경우
ImportError # 모듈은 있으나 없는 클래스나 메소드를 가져오려 할 때

# Practice 2

import random
class ClassHelper:
    def __init__(self, students):
        self.students = students

    def pick(self, n):
        choice = random.sample(self.students, n)
        return choice 

    def match_pair(self):
        pair = []
        random.shuffle(self.students)
        length = len(self.students)
        
        for i in range(0, length, 2):
            if i == length - 3:
                pair.append(self.students[i:])
                break
            else:
                pair.append(self.students[i:i+2])
        return pair

ch = ClassHelper(['김싸피', '이싸피', '조싸피', '박싸피', '정싸피'])

print(ch.pick(1))
print(ch.pick(1))
print(ch.pick(2))
print(ch.pick(3))
print(ch.pick(4))

print(ch.match_pair())


# class ClassHelper:
#     class_var = 0
#     import random
#     print('===== 클래스 내부 =====')
#     print(dir()) # 클래스 위치에 있는 이름들
#     def __init__(self, students):
#         self.students = students
#     def pick(self, n):
#         print('===== 인스턴스 내부 =====')
#         print(dir()) # 인스턴스 메서드 위치에 있는 이름들
#         pprint.pprint(globals())

# ch = ClassHelper(['김싸피', '이싸피', '조싸피', '박싸피', '정싸피'])

# print(ch.pick(1))