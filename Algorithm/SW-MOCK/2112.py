import copy
from itertools import combinations
T = int(input())

def check(films):
    clear = 0
    for i in range(W):
        A = B = 0
        for j in range(D):
            if films[j][i] > 0:
                B += 1
                A = 0
            else:
                A += 1
                B = 0
            if A == K or B == K:
                clear += 1
                break
    return clear

def Achem(film, t):
    for i in combinations(range(D), t):
        for j in i:
            for k in range(W):
                film[j][k] += 1
            if check(film) == W:
                return True
        for h in i:
            for l in range(W):
                film[h][l] -= 2
            if check(film) == W:
                return True
        for m in i:
            for n in range(W):
                film[m][n] += 1

def Bchem(film, t):
    for i in combinations(range(D), t):
        for j in i:
            for k in range(W):
                film[j][k] -= 1
            if check(film) == W:
                return True
        for h in i:
            for l in range(W):
                film[h][l] += 2
            if check(film) == W:
                return True
        for m in i:
            for n in range(W):
                film[m][n] -= 1

for tc in range(1, T+1):
    D,W,K = map(int, input().split())
    films = [list(map(int, input().split())) for _ in range(D)]
    success = check(films)
    if success == W:
        print('#{} {}'.format(tc, 0))
    else:
        for i in range(1, D+1):
            test = copy.deepcopy(films)
            if Achem(test, i) or Bchem(test, i):
                print('#{} {}'.format(tc, i))
                break