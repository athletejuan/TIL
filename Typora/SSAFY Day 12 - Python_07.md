# SSAFY Day 12 Python Day 7

## Object Oriented Programming(객체 지향 프로그래밍)



### 생성자와 소멸자



### 포켓몬 구현하기

* 예시: Python Ruby Warrior
  



### 인스턴스/클래스/스태틱 메서드(method)



class MyClass:
    def instance_method(self):
        return '저는 인스턴스 메서드 입니다.'
    @classmethod
    def class_method(cls):
        return f'저는 클래스 메서드 입니다. 저를 호출한 사람은 {cls}입니다.'

MyClass.class_method()



* 인스턴스 입장에서 확인해 봅시다.

mc = MyClass()

mc.class_method()



#### 연산자 오버로딩



class Person:
    population = 0
    

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1
        
    def greeting(self):
        print(f'{self.name} 입니다. 반갑습니다!')
        
    def __repr__(self):
        return f'< "name:" {self.name}, "age": {self.age} >'
    
    def __gt__(self, other):
        return self.age > other.age
    
    def __eq__(self, other):
        return self.age == other.age
    
    def __ge__(self, other):
        return self.age >= other.age