N = int(input())

square = [[0]*(N+2)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
apart = 0
downtown = []
for _ in range(N):
    square.append([0]+list(map(int, input()))+[0])
square.append([0]*(N+2))

def BFS(x):
    for k in range(4):
        if square[x[0]+dx[k]][x[1]+dy[k]] and [x[0]+dx[k], x[1]+dy[k]] not in town:
            town.append([x[0]+dx[k], x[1]+dy[k]])        
    square[x[0]][x[1]] = 0

for i in range(1, N+1):
    for j in range(1, N+1):
        if square[i][j]:
            town = [[i,j]]
            apart += 1
            num = 0
            while town:
                start = town.pop(0)
                num += 1
                BFS(start)
            downtown.append(num)
print(apart)
for d in sorted(downtown):
    print(d)