from sys import stdin


def cantor(N, line):
    if N < 3:
        print(line, end='')
    else:
        solid, blank = line[:N//3], ' '*(N//3)
        cantor(N//3, solid)
        cantor(N//3+1, blank)
        cantor(N//3, solid)


while True:
    N = stdin.readline().rstrip()
    if N == '': break
    N = 3**int(N)
    line = '-'*N

    cantor(N, line)
    print()