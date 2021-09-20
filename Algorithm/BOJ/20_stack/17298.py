N = int(input())
A = list(map(int, input().split()))
stack, top = [[A[0],0]], A[0]
answer = [-1] * N

for i in range(1, N):
    if A[i] > top:
        for j in range(len(stack)-1, -1, -1):
            if A[i] > stack[j][0]:
                answer[stack[j][1]] = A[i]
                stack.pop()
            else:
                break
    stack.append([A[i], i])
    top = A[i]
print(*answer)