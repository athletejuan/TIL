A,B = input().split()

def six(num):
    big = ''
    for n in num:
        if n == '5':
            n = '6'
        big += n
    return int(big)

def five(num):
    small = ''
    for n in num:
        if n == '6':
            n = '5'
        small += n
    return int(small)

print(five(A) + five(B), six(A) + six(B))