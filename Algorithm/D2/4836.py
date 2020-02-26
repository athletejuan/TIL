T = int(input())

for test_case in range(1, T+1):
    num = int(input())
    red = []
    blue = []
    count = 0
    for i in range(num):
        reg = list(map(int, input().split()))
        for x in range(reg[0], reg[2]+1):
            for y in range(reg[1], reg[3]+1):
                if reg[4]%2:
                    red.append((x,y))
                else:
                    blue.append((x,y))
    for j in red:
        if j in blue:
            count += 1
    print(f'#{test_case} {count}')