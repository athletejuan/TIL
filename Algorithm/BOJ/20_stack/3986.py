N = int(input())
good = 0

for i in range(N):
    word = list(input())
    stack = []
    for char in word:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    if not stack:
        good += 1
print(good)