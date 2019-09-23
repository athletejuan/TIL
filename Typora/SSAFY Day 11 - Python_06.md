# SSAFY Day 11 Python Day 6

## Error and Exception



try catch

except

else

finally

assert



## Object Oriented Programming(객체 지향 프로그래밍)



youtube > bill gates steve jobs, pc guy mac guy

* steve jobs 객체지향 프로그래밍(object-oriented programming)에 대한 미련, 아쉬움이 있을 정도
  * oop 이해가 중요



* 절차적 프로그래밍 - 사람의 사고 방식과는 다름.
  * 저장
  * 조건
  * 반복

* 객체 지향 프로그래밍 - 사람이 사고하는 방식대로 구현하고자 함

  * 논리학: 세상 모든 것은 단순하게 표현 가능하다 (주어 동사로 표현 가능).

  * 주어 / 서술어 관계로 구현

    * Student.objects.get(id =1) : 학생 개체 중 id가 1번인 학생을 가져온다.

      * 절차적 프로그래밍으로 표현하면

        ###### DB에 연결한다.

        ###### DB안에 있는 id 컬럼을 조회한다.

        ###### id = 1 값을 가져와 출력한다.

        

      * 객체 지향 프로그래밍

        ###### 'hello'.islower()

  * Class(군집, 종) 단위로 이해

  * Instance()

    * Class 의 한 단위
    * 예시

  * 속성(attribute)

  * 방법(method)



클래스 인스턴스 이름공간...(설명 어려움..;;;)



class Person:
    name = 'unknown'    
    def greeting(self):
        return f'{self.name} 입니다.'
    
p1 = Person()
p1.greeting()



p1.name  = 'juan'

p1