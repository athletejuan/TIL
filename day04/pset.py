# 1.평균 구하기
score = {
    '수학':80,
    '국어':90,
    '음악':100
}

sum = 0

for s in score:
    sum += score[s]

print(sum/len(score.keys()))

# 반별 평균
scores = {
    'a': {
    '수학':80,
    '국어':90,
    '음악':100
},
'b': {
   '수학':80,
   '국어':70,
   '음악':40 
}}

sum = 0

for s in scores['a']:
    sum += scores['a'][s]
print(sum/len(scores['a'].keys))

