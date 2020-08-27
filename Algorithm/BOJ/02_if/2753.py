y = int(input())
if not y % 4:
    if y % 100 or not y % 400:
        print('1')
    else:
        print('0')
else:
    print('0')