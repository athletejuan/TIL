import sys
input = sys.stdin.readline

N = int(input())
lines = [list(map(int, input().split())) for i in range(N)]
lines.sort()
length = 0
start = lines[0][0]
end = lines[0][1]

while True:
    for idx,line in enumerate(lines):
        if line[0] > end:
            length += end-start
            start = lines[idx][0]
            end = lines[idx][1]
            break
        else:
            if end < line[1]:
                end = line[1]
    else:
        break
length += end-start
print(length)