def check(num):
    if not num or int(num) < 10:
        return True
    else:
        if num[0] == num[-1]:
            return check(num[1:-1])
        else:
            return False
    
while True:
    palnum = input()
    if palnum == '0':
       break
    if check(palnum):
        print('yes')
    else:
        print('no')