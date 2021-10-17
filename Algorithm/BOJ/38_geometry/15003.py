M,N,R = map(float, input().split())
ax,ay,bx,by = map(int, input().split())

if ax > bx:
    ax,bx = bx,ax
if ay > by:
    ay,by = by,ay

distance = 3.14159265358979*ay*(R/N)*(bx-ax)/M + (by-ay)*(R/N)
if (R/N)*(ay+by) < distance:
    distance = (R/N)*(ay+by)
print(distance)