n = int(input())
nums = []
stack = []
breaker = True

for i in range(n):
    num = int(input())
    if not i:
        for j in range(num):
            stack.append('+')
            nums.append(j+1)
        stack.append('-')
        h = nums.pop()
    else:
        if nums and num == nums[-1]:
            stack.append('-')
            nums.pop()
        elif nums and num < nums[-1]:
            print('NO')
            breaker = False
            break
        else:
            for k in range(h+1,num+1):
                stack.append('+')
                nums.append(k)
            stack.append('-')
            h = nums.pop()
if breaker:
    for s in stack:
        print(s)