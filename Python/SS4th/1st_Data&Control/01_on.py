# Workshop

# 1. 세로로 출력하기
N = int(input())

for i in range(1, N+1):
    print(i)

# 2. 가로로 출력하기
N = int(input())

for i in range(N+1):
    print(i, end=' ')

# 3. 거꾸로 출력하기
N = int(input())

for i in range(N, 0, -1):
    print(i)

# 4. 거꾸로 출력하기(SWEA #1545)
N = int(input())

for i in range(N, -1, -1):
    print(i, end=' ')

# 5. N줄 덧셈(SWEA #2025)
N = int(input())

total = 0
for i in range(1, N+1):
    total += i

print(total)

# Homework

# 1. Python에서 사용할 수 있는 식별자(예약어)를 찾아 작성하시오.

import keyword
print(keyword.kwlist)

# 2. Python에서 float는 실수를 표현하는 과정에서 같은 값으로 일치되지 않는다.
#   (floating point rounding error)
#   따라서, 아래의 값을 올바르게 비교하기 위한 코드를 작성하시오.

num1 = 0.1 * 3
num2 = 0.3

import math
print(math.isclose(num1, num2))

# 3. 이스케이프 시퀀스 중 1) 줄 바꿈, 2) 탭, 3) 백슬래쉬를 작성하시오.

'\n'
'\t'
'\\'

# 4. 안녕, 철수야 를 string interpolation을 사용하여 출력하시오.

name = '철수'
print(__(a)__)

print(f'안녕, {name}야')

# 5. 다음 중, 형 변환 시 오류가 발생하는 것을 고르시오.

1) str(1)
2) int("30")
3) int(5)
4) bool("50")
5) int("3.5") <-

# 6. 두 개의 정수 n과 m이 주어졌을 때, 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 반복문을 사용하지 않고, 별(*) 문자를 이용하여 출력하시오.

n = 5
m = 9

print((('*' * n) + '\n') * m)

# 7. print 함수를 한 번만 사용하여 다음 문장을 출력하시오.

print('"파일은 C:\\Windows\\Users\\내문서\\Python에 저장이 되어있습니다."\n나는 생각했다. \'cd를 써서 git bash로 들어가봐야지\'')

# 8. 다음은 이차 방정식의 근을 찾는 수식이다. 이를 파이썬 코드로 작성하시오.

answer1 = ((b * -1) + ((b ** 2) - 4 * a * c) ** .5) / (2 * a)
answer2 = ((b * -1) - ((b ** 2) - 4 * a * c) ** .5) / (2 * a)