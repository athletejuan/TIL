C = int(input())

for _ in range(C):
    uri = input().split('%2')
    for i in uri:
        if i:
            if i[0] == '0':
                i = i.replace('0',' ',1)
            elif i[0] == '1':
                i = i.replace('1','!',1)
            elif i[0] == '4':
                i = i.replace('4','$',1)
            elif i[0] == '5':
                i = i.replace('5','%',1)
            elif i[0] == '8':
                i = i.replace('8','(',1)
            elif i[0] == '9':
                i = i.replace('9',')',1)
            elif i[0] == 'a':
                i = i.replace('a','*',1)
            print('{}'.format(i), end="")
    print()