N = int(input())

quad = []
result = ''
for _ in range(N):
    quad.append(list(input()))
def quadtree(N,x,y):
    global quad, result
    e = N//2
    color = quad[y][x]
    breaker = False
    for i in range(x, x+N):
        if breaker:
            break
        for j in range(y, y+N):
            if quad[j][i] != color:
                result += '('
                quadtree(e,x,y)
                quadtree(e,x+e,y)
                quadtree(e,x,y+e)
                quadtree(e,x+e,y+e)
                result += ')'
                
                breaker = True
                break
    if not breaker:
        if color == '1':
            result += '1'
        else:
            result += '0'

quadtree(N,0,0)
print(result)