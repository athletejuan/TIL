import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
w, b = 0, 0

def color(p):
    length = len(p)
    check = p[0][0]
    for i in range(length):
        for j in range(length):
            if check != p[i][j]:
                return True
    return False

def quater(p):
    global b,w
    if color(p):
        length = len(p)//2
        div = []
        for i in range(2):
            for j in range(2):
                q = []
                for k in range(length):
                    row = []
                    for l in range(length):
                        row.append(p[i*length+k][j*length+l])
                    q.append(row)
                div.append(q)
        for q in div:
            if color(q):
                quater(q)
            else:
                if q[0][0]:
                    b += 1
                else:
                    w += 1
    else:
        if p[0][0]:
            b += 1
        else:
            w += 1

quater(paper)
print(w)
print(b)