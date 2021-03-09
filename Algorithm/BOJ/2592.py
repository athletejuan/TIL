nums = [0] * 100
avg, now = 0, 0

for i in range(10):
    num = int(input())//10
    avg += num
    nums[num] += 1

for j in range(1,100):
    if nums[j] > now:
        now = nums[j]
        mode = j*10

print(avg)
print(mode)