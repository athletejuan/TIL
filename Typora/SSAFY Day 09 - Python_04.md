# SSAFY Day 09



* 함수 타입
  * destructive(원본 파괴)
    * return(x) - 일반적으로 리턴하지 않음
  * non-destructive(원본 유지)
    * return(o) - 일반적으로 리턴



* join 함수

a = "This is Awesome".split(' ')

a.split(' ')

''.join(a) 

 = ThisisAwesome

' '.join(a)

 = This is Awesome



복사(Copy)



- 파이썬에서 모든 변수는 객체의 주소를 가지고 있을 뿐입니다.

```
num = [1, 2, 3]
```

- 위와 같이 변수를 생성하면 num이라는 객체를 생성하고, 변수에는 객체의 주소가 저장됩니다.
- 변경가능한(mutable) 자료형과 변경불가능한(immutable) 자료형은 서로 다르게 동작합니다.

따라서, 복사를 하고 싶을 때에는 다음과 같이 해야한다.

![1563417097331](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1563417097331.png)



num 은  숫자 자체가

list는 주소가 연결



* shallow copy

![1563422189276](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1563422189276.png)



* deep copy

![1563422121520](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1563422121520.png)



* comparison(shallow : deep)

![1563422338662](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1563422338662.png)



![1563422754782](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1563422754782.png)





|      | String | List | Dictionary | Set                        |
| ---- | ------ | ---- | ---------- | -------------------------- |
| C    |        |      |            | add()                      |
| R    |        |      |            |                            |
| U    |        |      |            | update()                   |
| D    |        |      |            | remove(), discard(), pop() |

