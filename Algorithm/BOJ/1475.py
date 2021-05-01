N = int(input())
nums = [0] * 9
sixnine, numset = 0, 1

while N:
    if N%10 == 6 or N%10 == 9:
        if sixnine:
            sixnine = 0
        else:
            nums[6] += 1
            sixnine = 1
    else:
        nums[N%10] += 1
    N //= 10

for i in range(9):
    if numset < nums[i]:
        numset = nums[i]
print(numset)