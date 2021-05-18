n = int(input())

for i in range(n):
    student = input().split()
    name = student[0]
    if len(student[2]) < 2:
        student[2] = '0'+student[2]
    if len(student[1]) < 2:
        student[1] = '0'+student[1]
    birth = int(student[3]+student[2]+student[1])
    if not i:
        old = young = [name, birth]
    else:
        if birth > young[1]:
            young = [name, birth]
        if birth < old[1]:
            old = [name, birth]
print(young[0])
print(old[0])