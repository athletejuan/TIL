def q2(number):
    multi = 1
    for i in str(number):
        multi *= int(i)
    return multi 
    
print(q2(123))
print(q2(2020))
print(q2(123456789))