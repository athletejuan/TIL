N = int(input())

def GCD(x,y):
    if x < y:
        x,y = y,x
    while y:
        x,y = y, x%y
    return x

min_gap, total_gap, a = 0, 0, 0
for _ in range(N):
    if not a:
        a = int(input())
    else:
        b = int(input())
        total_gap += b - a
        if not min_gap:
            min_gap = b - a
        else:
            min_gap = GCD(min_gap, b-a)
        a = b

min_tree = total_gap//min_gap - N + 1
print(min_tree)