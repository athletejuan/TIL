serial = map(int, input().split())
check = 0
for num in serial:
    check += num**2
print(check%10)