N = input()

nums = []
total = 0
check = False
for n in N:
    nums.append(n)
    total += int(n)
    if not int(n):
        check = True
if not total % 3 and check:
    print(''.join(reversed(sorted(nums))))
else:
    print(-1)