T = int(input())

for tc in range(T):
    k = int(input())
    n = int(input())
    
    start = [1, 1]
    for i in range(k+n-1):
        next_step = [1]
        for j in range(len(start)-1):
            next_step.append(start[j] + start[j+1])
        next_step += [1]
        start = next_step
    print(start[n-1])

# 재귀 시간초과
# def apart(k,n):
#     if n == 1:
#         return 1
#     elif not k:
#         return n
#     else:
#         return apart(k-1,n) + apart(k, n-1)

# for tc in range(T):
#     k = int(input())
#     n = int(input())
#     print(apart(k,n))