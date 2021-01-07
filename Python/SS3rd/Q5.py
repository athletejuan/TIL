def stairs(number):
    if number < 10:
        return True
#     if str(number)
    li = []
    for i in str(number):
        if not li:
            li.append(int(i))
        elif int(i) == int(li[-1])+1 or int(i) == int(li[-1])-1:
            li.append(int(i))
        else:
            return False
    return True
print(stairs(8))
print(stairs(79))
print(stairs(5567))
print(stairs(4343456))
print(stairs(89098))