# Workshop

# 1. 간단한 N의 약수(SWEA #1933)

# 입력으로 1개의 정수 N이 주어진다.
# 정수 N의 약수를 오름차순으로 출력하는 프로그램을 작성하라.

# [제약사항] N은 1이상 1,000이하의 정수이다. (1 ≤ N ≤ 1,000)
# [입력] 입력으로 정수 N이 주어진다.
# [출력] 정수 N의 모든 약수를 오름차순으로 출력한다.

N = int(input())

for i in range(1, N+1):
    if not N % i:
        print(i, end=' ')

# 2. 계단만들기

# 자연수 N을 입력 받아, 아래와 같이 높이가 N인 내려가는 계단을 출력하시오.
# [예시] N이 4일 경우, 아래와 같이 출력됩니다.

# 1
# 1 2
# 1 2 3
# 1 2 3 4

N = int(input())

for i in range(1, N+1):
    floor = ''
    for j in range(i):
        floor += (str(j+1) + ' ')
    print(floor)

for i in range(1, N+1):
    for j in range(1, i):
        print(j, end=' ')
    print(i)

# 3. 구구단

for i in range(2, 10):
    print(f'------ [{i}단] ------')
    for j in range(1, 10):
        print(f'{i} x {j} = {i*j}')
    print()

# Homework

# 1. 제시 된 컨테이너들을 각각, 변경 가능한 것(mutable)과 변경 불가능한 것(immutable)으로 분류하시오.

string, tuple, range => immutable
list, set, dictionary => mutable

# 2. range와 slicing을 활용하여 1부터 50까지 숫자 중 홀수로 이루어진 리스트를 만드시오.

a = list(range(1, 51))
# b = a[0:-1:2]
b = a[::2]
print(b)

# 3. 반 학생들의 정보를 이용하여 key는 이름, value는 나이인 dictionary를 만드시오.

student_dict = {
    '최정휴':30,
    '고영길':28
}

# 4. 두 개의 정수 n과 m이 주어졌을 때, 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 별(*) 문자를 이용하여 출력하시오. 단, 반복문을 사용하여 작성하시오.

n = int(input())
m = int(input())

for i in range(m):
    print('*'*n)

for height in range(m):
    for width in range(n):
        print('*', end='')
    print()

# 5. 제시된 if문을 조건 표현식으로 바꾸어 작성하시오.

temp = 36.5
# if temp >= 37.5:
#     print('입실 불가')
# else:
#     print('입실 가능')

print('입실 불가') if temp >= 37.5 else print('입실 가능')

# 6. 제시된 list의 평균 값을 출력하시오.

scores = [80, 89, 99, 83]

result = 0
for num in scores:
    result += num
print(result / len(scores))

average = sum(scores)/len(scores)
print(average)

# Practice 1

# 1. 갯수 구하기

students = ['김철수', '이영희', '조민지']

print(len(students))

result = 0
for student in students:
    result = result + 1
    # result += 1
print(result)

# 2. 득표수 구하기

students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']

count = 0
for student in students:
    if student == '이영희':
        count += 1
print(count)

# 3. 최대값 구하기

N = [7, 10, 22, 4, 3, 17]

# print(max(numbers))
# print(sorted(numbers[-1]))
# 메모리 제한 걸릴 수 있음

max_num = 0
# 항목들이 모두 음수값이면 0이 출력될 수 있으니 첫번째 값으로 초기화하는 것이 나음
# max_num = N[0]

for num in N:
    if num > max_num:
        max_num = num
print(max_num)

# 4. 최소값 구하기

min_num = N[0]

for num in N:
    if num < min_num:
        min_num = num
print(min_num)

# 5. 최대값과 등장 횟수 구하기

numbers = [7, 10, 22, 7, 22, 22]

max_num = numbers[0]
count = 0

for num in numbers:
    if num > max_num:
        max_num = num
        count = 1
    elif num == max_num:
        count += 1
print(max_num, count)

# 6. 5의 개수 구하기

N = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]

count_five = 0

for num in N:
    if num == 5:
        count_five += 1
print(count_five)

# 7. 'a'가 싫어

W = input()

new = ''
for char in W:
    if char != 'a':
        new += char
print(new)

# 8. 단어 뒤집기

re = ''
for char in W:
    re = char + re
print(re)

re = W[::-1]
print(re)

# 9. 회문 판별하기(extra)

for i in range(len(W)):
    if W[i] != W[-i-1]:
        print('N')
        break
else:
    print('Y')

# Practice 2

# 1. 더블더블

# 자연수 N을 입력 받아, 1부터 주어진 자연수까지 홀수는 2, 짝수는 3을 곱한 값(들)을 출력하시오.
# [제약 사항] 주어질 숫자는 30을 넘지 않는다.

N = int(input())

s = 0
for i in range(1, N+1):
    if i % 2:
        # print(i*2)
        s += i*2
    else:
        # print(i*3)
        s += i*3
print(s)

# 2. 간단한 소수 판별 1
# 간단한 소수 판별

# 입력으로 1개의 정수 N이 주어진다.
# 정수 N이 소수인지 아닌지 판별하여 출력하시오.

# [제약사항] N은 2이상 1,000이하의 정수이다. (2 ≤ N ≤ 1,000)
# [입력] 입력으로 정수 N이 주어진다.
# [출력] 정수 N이 소수이면 'Y', 소수가 아니면 'N'을 출력한다.

number = int(input())

is_prime = 'Y'
for i in range(2, number):
    if number % i == 0:
        is_prime = 'N'
        # 추가
        break
print(is_prime)

for i in range(2, number):
    if not number % i:
        print('N')
        break
else:
    print('Y')

# 3. 간단한 소수 판별 2
# 조건, 반복문을 응용하여 numbers 리스트의 요소들이 소수인지 아닌지 판단하는 코드를 작성하시오.

# [출력]
# 26은(는) 소수가 아닙니다. 2은(는) 26의 인수입니다.
# 39은(는) 소수가 아닙니다. 3은(는) 39의 인수입니다.
# 51은(는) 소수가 아닙니다. 3은(는) 51의 인수입니다.
# 53은(는) 소수입니다.
# 57은(는) 소수가 아닙니다. 3은(는) 57의 인수입니다.
# 79은(는) 소수입니다.
# 85은(는) 소수가 아닙니다. 5은(는) 85의 인수입니다.

numbers = [26, 39, 51, 53, 57, 79, 85]

for number in numbers:
    # 1. 아래는 동일
    is_prime = 'Y'
    for i in range(2, number):
        if number % i == 0:
            is_prime = 'N'
            break
    # 2. 값에 따라 다른 출력.
    if is_prime == 'Y':
        print(f'{number}은(는) 소수입니다.')
    else:
        print(f'{number}은(는) 소수가 아닙니다. {i}은(는) {number}의 인수입니다.')

for number in numbers:
    for i in range(2, number):
        if not number % i:
            print(f'{number}은(는) 소수가 아닙니다. {i}은(는) {number}의 인수입니다.')
            break
    else:
        print(f'{number}은(는) 소수입니다.')

# 4. 두 번째로 많은 수의 개수 구하기(extra)

N = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]

many = set()
for i in N:
    many.add(N.count(i))
print(sorted(many)[-2]) # 두 번째로 많은 수의 개수
for j in N:
    if N.count(j) == sorted(many, reverse=True)[1]:
        print(j)    # 두 번째로 많은 수를 출력
        break

# 5. 자릿수 더하기(SWEA #2058) (extra)
# 자연수 n을 입력 받아, 각 자릿수의 합을 계산하여 출력하시오.

# [제약 사항] 자연수 n은 1부터 9999까지의 자연수이다. (1 ≤ n ≤ 9999)
# [입력] 입력으로 자연수 n이 주어진다.
# [출력] 각 자릿수의 합을 출력한다.

n = input()

s = 0
for char in n:
    s += int(char)
print(s)

n = int(input())

s = 0
while n:
    s += n % 10
    n = n//10
print(s)

# 6. Collatz 추측 (extra)
N = int(input())

count = 0
while N != 1:
    if N % 2:
        N = N*3 + 1
    else:
        N /= 2
    count += 1
    if count == 500:
        print(-1)
        break
if count != 500:
    print(count)

for i in range(500):
    if N%2 == 0:
        N = N/2
    else:
        N = N*3+1
    
    if N == 1:
        i += 1
        print(i)
        break

    if i+1 >= 500:
        print(-1)
        break