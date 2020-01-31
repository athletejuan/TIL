def q6(number):
    if number < 100:
        return False
    num = str(number)
    for i in range(1, len(num)-1):
        if num[i-1] == num[i+1]:
            return True
    return False

print(q6(8))
print(q6(155))
print(q6(1555))
print(q6(2020))
print(q6(414092133))