a,b,c,d,e,f = map(int, input().split())

if not a:
    y = c//b
    x = (f-(e*(c//b)))//d
elif not d:
    y = f//e
    x = (c-(b*(f//e)))//a
else:
    m = a
    a,b,c = d*a, d*b, d*c
    d,e,f = m*d, m*e, m*f

    if a == d:
        y = (f-c)//(e-b)
        x = (c-(b*y))//a
    else:
        y = (f+c)//(e+b)
        x = (c+(b*y))//a

print(x,y)