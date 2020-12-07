T = int(input())

for _ in range(T):
    quiz = input()
    right = 1
    total = 0
    for i in quiz:
        if i == 'O':
            total += right
            right += 1
        else:
            right = 1
    print(total)