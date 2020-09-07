T = int(input())

for t in range(T):
    limit = int(input())
    time = list(map(int, input().split()))
    if sum(time) <= limit:
        print('YES')
    else:
        print('NO')