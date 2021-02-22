w,h = map(int, input().split())
p,q = map(int, input().split())
t = int(input())
s = t

t -= w-p
s -= h-q
x = t%w if (t//w)%2 else w - (t%w)
y = s%h if (s//h)%2 else h - (s%h)

print(x,y)