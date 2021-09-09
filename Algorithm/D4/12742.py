T = int(input())
 
top, gaps = 0, []
for _ in range(1, T+1):
    a,b = map(int, input().split())
    gap = b-a
    gaps.append([gap, a])
    if top < gap:
        top = gap
 
rains = [0, 1] + [0] * top
for i in range(1, top):
    rains[i+1] = rains[i] + i + 1
 
for tc in range(1, T+1):
    print('#{} {}'.format(tc, rains[gaps[tc-1][0]-1]-gaps[tc-1][1]))