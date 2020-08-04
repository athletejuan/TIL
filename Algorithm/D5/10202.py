T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    count = 0
    chars = []
    for i in range(3):
        for j in input():
            chars.append(j)
    for _ in range(n):
        match = set()
        for k in range(3):
            match.add(chars[k*n+_])
        if len(match) == 3:
            count += 2
        elif len(match) == 2:
            count += 1
    print(f'#{test_case} {count}')