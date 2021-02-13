A,B = map(int, input().split())

n = 0
start = 0
end = 0
while end < B:
    n += 1
    end += n
    d = end - B
    if end >= A-1 and not start:
        s = n
        start = end
        g = start - A + 1

plus = 0
minus = 0
for i in range(1, n+1):
    plus += i**2
plus -= i*d
for j in range(1, s+1):
    minus += j**2
minus -= j*g
print(plus-minus)