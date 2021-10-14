from collections import deque
import sys
input = sys.stdin.readline

P = 0
dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

def BFS():
    q = deque([[0, 0]])
    while q:
        r,c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if thief[nr][nc] > thief[r][c] + cave[nr][nc]:
                    thief[nr][nc] = thief[r][c] + cave[nr][nc]
                    q.append([nr, nc])
    return thief[N-1][N-1] + cave[0][0]


while True:
    P += 1
    N = int(input())
    if not N:
        break
    cave = [list(map(int, input().split())) for _ in range(N)]
    thief = [[N**2*9]*N for _ in range(N)]
    thief[0][0] = 0
    print('Problem {}: {}'.format(P, BFS()))