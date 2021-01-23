S = input()
password = ''
for i in S:
    if ord(i) > 109 or 97 > ord(i) > 77 :
        password += chr(ord(i)-13)
    elif ord(i) > 96 or 78 > ord(i) > 64:
        password += chr(ord(i)+13)
    else:
        password += i
print(password)