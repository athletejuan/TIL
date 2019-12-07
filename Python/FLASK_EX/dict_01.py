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
