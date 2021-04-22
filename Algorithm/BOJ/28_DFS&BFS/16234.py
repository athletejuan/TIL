# PyPy3로 pass, Python3는 80% 시간초과
import sys
input = sys.stdin.readline

N,L,R = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(N)]
earth, cnt = [], 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS():
    global earth
    earth = []
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                ally = [[i,j]]
                union = [[i,j]]
                total = 0
                while ally:
                    x,y = ally.pop()
                    total += country[x][y]
                    visited[x][y] = 1
                    for k in range(4):
                        a,b = x+dx[k], y+dy[k]
                        if 0 <= a < N and 0 <= b < N and L <= abs(country[x][y] - country[a][b]) <= R and not visited[a][b]:
                            ally.append([a,b])
                            union.append([a,b])
                            visited[a][b] = 1
                union.append(total//len(union))
                earth.append(union)
    return False if len(earth) == N**2 else True

while BFS():
    for a in earth:
        for j in range(len(a)-1):
            country[a[j][0]][a[j][1]] = a[-1]
    cnt += 1

print(cnt)


# import sys
# input = sys.stdin.readline
#
# N,L,R = map(int, input().split())
# country = [list(map(int, input().split())) for _ in range(N)]
# earth = []
# cnt = 0
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
# def BFS():
#     global earth
#     earth = []
#     visited = [[0] * (N) for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             if not visited[i][j]:
#                 population = [country[i][j]]
#                 ally = [[i,j]]
#                 union = [[i,j]]
#                 total = 0
#                 while ally:
#                     x,y = ally.pop()
#                     p = population.pop()
#                     total += p
#                     visited[x][y] = 1
#                     for k in range(4):
#                         a,b = x+dx[k], y+dy[k]
#                         if 0 <= a < N and 0 <= b < N and L <= abs(p - country[a][b]) <= R and not visited[a][b]:
#                             ally.append([a,b])
#                             union.append([a,b])
#                             population.append(country[a][b])
#                             visited[a][b] = 1
#                 each = total // len(union)
#                 earth.append([union, each])
#     return False if len(earth) == N**2 else True
#
# while BFS():
#     for i in earth:
#         for j in range(len(i[0])):
#             country[i[0][j][0]][i[0][j][1]] = i[1]
#     cnt += 1
#
# print(cnt)