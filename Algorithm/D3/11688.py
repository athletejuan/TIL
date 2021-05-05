T = int(input())

def CWL(a,b):
    return [a, a+b]

def CWR(a,b):
    return [a+b, b]

def GCD(a,b):
    if a < b:
        a,b = b,a
    while b:
        a,b = b,a%b
    return a

for tc in range(1, T+1):
    CW = input()
    a,b = 1,1
    for node in CW:
        if node == 'L':
            a,b = CWL(a,b)
        else:
            a,b = CWR(a,b)
    print('#{} {} {}'.format(tc, a//GCD(a,b), b//GCD(a,b)))