N = int(input())
students = []

for i in range(N):
    student = input().split()
    for j in range(1, 4):
        student[j] = int(student[j])
    students.append(student)

for name in sorted(students, key=lambda x: (-x[1], x[2], -x[3], x[0])):
    print(name[0])