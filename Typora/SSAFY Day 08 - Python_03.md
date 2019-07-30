# SSAFT Day 08

## Homeworkshop 문제풀이

* 중복 단어 세기
* from collections import Counter



* URL 만들기, 검증하기

* 이름공간, 스코프

* 재귀함수

  * 팩토리얼

    def factorial(n):
        if n == 1:
            return 1
        else:
            return n * factorial(n-1)

    

  * 피보나치

    def fib(n):
        if n == 0 or n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)
    fib(4)

    

  * 하노이의 탑