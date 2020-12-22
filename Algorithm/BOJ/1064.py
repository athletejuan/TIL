ax, ay, bx, by, cx, cy = map(int, input().split())

d = []
d.append(((ax-bx)**2+(ay-by)**2)**.5)
d.append(((ax-cx)**2+(ay-cy)**2)**.5)
d.append(((bx-cx)**2+(by-cy)**2)**.5)

s = sorted(d)
if (ax-bx)*(ay-cy) == (ay-by)*(ax-cx):
    print(-1)
else:
    print(2*(s[2]-s[0]))