# 1. problem.txt 파일 생성 후 다음과 같은 내용 작성
0
1
2
3

# 2. problem.txt 파일 내용을 다음과 같이 변경
3
2
1
0


with open('problem.txt','w') as f:
    for i in range(4):        
        f.write(f'{i}\n')

re = []
with open('problem.txt','r') as f:
    for i in reversed(list(f.readlines())):
        re.append(f'{i}')
with open('problem.txt','w') as f:
    for i in re:
        f.write(f'{i}')