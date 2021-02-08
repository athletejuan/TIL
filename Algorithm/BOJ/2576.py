total = 0
min_odd = 0
for _ in range(7):
    num = int(input())
    if num % 2:
        total += num
        if not min_odd or min_odd > num:
            min_odd = num
if not total:
    print(-1)
else:
    print(total)
    print(min_odd)