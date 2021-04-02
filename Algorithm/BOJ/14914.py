a,b = map(int, input().split())

def GCD(x,y):
    if not y:
        return x
    if x < y:
        x,y = y,x
    x,y = y,x%y
    return GCD(x,y)

G = GCD(a,b)
for i in range(1, G//2+1):
    if not G%i:
        print(i, a//i, b//i)
print(G, a//G, b//G)