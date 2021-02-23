n = int(input())
Quadrant = [0] * 4
Axis = [0]

for tc in range(n):
    x,y = map(int, input().split())
    if not x or not y:
        Axis[0] += 1
    elif x > 0 and y > 0:
        Quadrant[0] += 1
    elif x < 0 and y > 0:
        Quadrant[1] += 1
    elif x < 0 and y < 0:
        Quadrant[2] += 1
    else:
        Quadrant[3] += 1

for idx, Q in enumerate(Quadrant):
    print('Q{}: {}'.format(idx+1, Q))
print('AXIS: {}'.format(Axis[0]))