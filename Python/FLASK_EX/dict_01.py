'''
Python dictionary Practice
'''

# 1. 평균을 구하시오.
scores = {
    '수학': 80,
    '국어': 90,
    '과학': 100,
}

print('==== Q1 ====')

sum_score = 0
for score in scores.values():
    sum_score += score
result = sum_score / len(scores)
print(result)

# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '과학': 100
    },
    'b': {
        '수학': 70,
        '국어': 85,
        '과학': 100
    }
}

print('==== Q2 ====')

sum_score = 0
count = 0

for person_score in scores.values():
    for subject_score in person_score.values():
        sum_score += subject_score
        count += 1
result = sum_score / count
print(result)

# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')

for key, value in city.items():
    temps = 0
    for t in value:
        temps += t
    temp = temps / len(value)
    print(f'{key}: {temp}')

# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')

count = 0
for key, value in city.items():
    if count == 0:
        hot_temp = max(value)
        cold_temp = min(value)
        hot_city = key
        cold_city = key
        count += 1
    else:
        if max(value) > hot_temp:
            hot_temp = max(value)
            hot_city = key
        if min(value) < cold_temp:
            cold_temp = min(value)
            cold_city = key
print(hot_city, hot_temp, cold_city, cold_temp)

# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?
# == 서울 온도 리스트에 2가 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')

if 2 in city['서울']:
    print('예')
else:
    print('아니오')