def q2(num):
    if (num % 10) % 2 == 0:
        if (num % 100) % 3 == 0:
            if num % 4 == 0:
                return True
    else:
        return False
        
print(q2(512))
print(q2(384))
print(q2(321))