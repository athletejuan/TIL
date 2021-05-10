n,m = map(int, input().split(':'))

def reduction(a,b):
    while b:
        if a < b:
            a,b = b,a
        a,b = b,a%b
    return a

print('{}:{}'.format(n//reduction(n,m), m//reduction(n,m)))