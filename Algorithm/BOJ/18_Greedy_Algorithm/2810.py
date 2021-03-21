N = int(input())
seats = list(input())
count = 0

for seat in seats:
    if seat == 'L':
        count += 1
if not count:
    print(N)
else:
    print(N+1-(count//2))