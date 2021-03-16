N = int(input())
trophy = [int(input()) for _ in range(N)]

left, right = 0, 0
def view(x):
    global left_cnt, right_cnt
    for j in range(x):
        if trophy[x] <= trophy[j]:
            left_cnt = 0
        if trophy[N-1-x] <= trophy[N-1-j]:
            right_cnt = 0

for i in range(N):
    left_cnt, right_cnt = 1, 1
    view(i)
    left += left_cnt
    right += right_cnt

print(left)
print(right)