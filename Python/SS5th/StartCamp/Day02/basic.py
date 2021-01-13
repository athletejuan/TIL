# 숫자
number1 = 3
number2 = 3.14
print(type(number1))
print(type(number2))

# 문자
string = '문자열'
print(type(string))

# boolean
boolean = True
print(type(boolean))

# F-string
# F-string / string interpolation
name = '홍길동'
print(f'{name}입니다. 반갑습니다.')

# List
# 리스트 선언
my_list = ['java', 'django']

# 리스트 원소 접근
print(my_list[0])

# 리스트 원소 변경
my_list[0] = 'python'

# 리스트 원소 접근
print(my_list[0])

# 리스트 길이
print(len(my_list))

# 미니 실습
# 1. 어제 먹은 음식들로 채워진 리스트를 만들어보시오.
foods = ['피자', '치킨', '샐러드']

# 2. 첫번째 음식을 출력하시오.
print(foods[0])

# 3. 두번째 음식을 초밥으로 바꾸시오.
foods[1] = '초밥'
print(foods[1])

# Dictionary
# 딕셔너리 선언
my_home = {
    "location": "seoul",
    "area-code": "02",
}

# 딕셔너리 원소 접근
print(my_home['location'])
# print(my_home['name'])
print(my_home.get('location'))
print(my_home.get('name'))

# 딕셔너리 원소 변경
my_home['location'] = 'gumi'
print(my_home['location'])

# 미니 실습1

# 1-1. 자신의 이름, 나이, 인사말로 구성된 my_info dictionary를 만들어보시오.
# (name, age, msg)
my_info = {
    "name": "hacking",
    "age": "100",
    "msg": "Show me your code"
}
print(my_info)


#1-2. my_info 딕셔너리에서 나이만 출력하시오.
print(my_info['age'])

# 미니 실습2

coin = {
    "BTC": {
        "opening_price": "44405000",
        "closing_price": "38806000",
        "min_price": "36640000",
        "max_price": "44999000",
        "prev_closing_price": "44404000",
        "fluctate_24H": "-7463000",
        "fluctate_rate_24H": "-16.13"
    },
    "ETH": {
        "opening_price": "1458000",
        "closing_price": "1229000",
        "min_price": "1100000",
        "max_price": "1490000",
        "prev_closing_price": "1458000",
        "fluctate_24H": "-275000",
        "fluctate_rate_24H": "-18.28"
    },
    "XRP": {
        "opening_price": "364.5",
        "closing_price": "311.9",
        "min_price": "284.2",
        "max_price": "372.7",
        "prev_closing_price": "364.2",
        "fluctate_24H": "-90.6",
        "fluctate_rate_24H": "-22.51"
    }
}

# 2-1. 코인의 정보에서 BTC의 최대 가격을 출력하시오.
print(coin['BTC']['max_price'])

# 2-2. ETH의 시가와(opening price) XRP의 시가를 더한 결과를 출력하시오.
total_opening_price = int(coin['ETH']['opening_price']) + float(coin['XRP']['opening_price'])
print(total_opening_price)


movie = {
    "movieInfo": {
        "movieNm": "광해, 왕이 된 남자",
        "movieNmEn": "Masquerade",
        "showTm": "131",
        "prdtYear": "2012",
        "openDt": "20120913",
        "typeNm": "장편",
        "nations": [
            {
            "nationNm": "한국"
            }
        ],
        "genres": [
            {
            "genreNm": "사극"
            },
            {
            "genreNm": "드라마"
            }
        ],
        "directors": [
            {
            "peopleNm": "추창민",
            "peopleNmEn": "CHOO Chang-min"
            }
        ],
        "actors": [
            {
            "peopleNm": "이병헌",
            "peopleNmEn": "LEE Byung-hun",
            "cast": "광해/하선"
            },
            {
            "peopleNm": "류승룡",
            "peopleNmEn": "RYU Seung-ryong",
            "cast": "허균"
            },
            {
            "peopleNm": "한효주",
            "peopleNmEn": "HAN Hyo-joo",
            "cast": "중전"
            }
        ]
    }
}

# 1. 영화의 제목을 출력하시오.
print(movie['movieInfo']['movieNm'])

# 2. 영화감독의 영어 이름을 출력하시오.
print(movie['movieInfo']['directors'][0]['peopleNmEn'])

# 3. 영화에 출연한 배우가 몇명인지 출력하시오.
print(len(movie['movieInfo']['actors']))
# print(len(movie.get('movieInfo').get('actors')))


# 기초 연산자
# 산술 연산자
print(3 + 5)
print(5 - 3)
print(100 * 5)
print(100 / 3)
print(100 // 3)
print(100 % 3)
print(2 ** 5)

# 비교 연산자
print(5 == 5)
print(3 == '3')
print(3 != 5)
print(3 >= 3)
print(5 < 4)

# 조건문
n = 10

# 1. 주어진 양수 n이 홀수, 짝수인지 판별하여 출력하는 코드를 작성하시오.
if n % 2 == 1:
	print('홀수')
else:
	print('짝수')

# 2. 주어진 숫자 n이 양수, 0, 음수인지 판별하여 출력하는 코드를 작성하시오.
if n > 0:
	print('양수')
elif n == 0:
	print('0')
else:
	print('음수')


# 반복문
numbers = [1, 2, 3]

for number in numbers:
	print(number)

# 미니 실습

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 리스트의 원소 중에서 홀수만 찾아 그 값을 출력하시오
# 예시 
"""
1은(는) 홀수입니다.
3은(는) 홀수입니다.
5은(는) 홀수입니다.
7은(는) 홀수입니다.
9은(는) 홀수입니다.
"""

for number in numbers:
    if number % 2 == 1:
        print(f'{number}은(는) 홀수입니다.')


# EXTRA
# 함수
# 함수 정의
def sum(a, b):
	result = a + b
	return result

# 함수 실행
sum(1, 5)
print(sum(1, 5))

# 함수 실행 결과 저장하기
result = sum(1, 5)
print(result)


# 미니 실습

# 1-1. 두 수의 곱을 계산하는 함수 mul을 만드시오.
def mul(a, b):
	return a * b

print(mul(2, 4))

# 1-2. 주어진 양수 n이 짝수인지 판별하여 True/False를 반환하는 함수를 작성하시오.
def is_even(n):
	if n % 2 == 1:
		result = False
	else:
		result = True
	return result

print(is_even(4))
print(is_even(5))