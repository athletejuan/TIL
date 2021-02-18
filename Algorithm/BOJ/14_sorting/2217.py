N = int(input())
nums = []
m = 0

for _ in range(N):
    now = int(input())
    nums.append(now)

sn = sorted(nums)
for j in range(N):
    w = sn[j]*(N - j)
    if w > m:
        m = w
print(m)