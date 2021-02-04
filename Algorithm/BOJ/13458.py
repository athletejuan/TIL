N = int(input())
students = list(map(int, input().split()))
B,C = map(int, input().split())

for student in students:
    if student - B > 0:
        N += (student - B) // C
        if (student - B) % C:
            N += 1
print(N)