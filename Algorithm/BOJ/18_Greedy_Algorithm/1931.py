N = int(input())

meeting = sorted([list(map(int, input().split())) for _ in range(N)])
meeting = sorted(meeting, key=lambda x: x[1])
fin = cnt = 0

for meet in meeting:
    if meet[0] >= fin:
        fin = meet[1]
        cnt += 1
print(cnt)