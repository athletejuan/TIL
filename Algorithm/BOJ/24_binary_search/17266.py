N = int(input())
M = int(input())
lights = list(map(int, input().split()))
height = 0

for light in lights:
    if not height:
        height = light
    else:
        if height < (light - before + 1)//2:
            height = (light - before + 1)//2
    before = light
if N-light < height:
    print(height)
else:
    print(N-light)