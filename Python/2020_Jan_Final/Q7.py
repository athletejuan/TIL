def q7(num):
    cnt = 0 
    for i in range(100, 1000):
        if (i//100 + i % 10) == num and len(set(str(i))) == 3 and (len(set(str(i)) & set('012345')) == 3):
            print(i)
            cnt += 1
    return cnt

print(q7(1))
print(q7(2))
print(q7(3))
print(q7(4))
print(q7(5))
print(q7(6))
print(q7(7))
print(q7(8))
print(q7(9))