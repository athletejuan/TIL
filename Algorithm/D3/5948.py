T = int(input())

for test_case in range(1, T+1):
    numbers = list(map(int, input().split()))
    sum_tri = []
    for i in range(len(numbers)-2):
        tri = []
        tri.append(numbers[i])
        for j in range(i+1, len(numbers)-1):
            tri.append(numbers[j])
            for k in range(j+1, len(numbers)):
                tri.append(numbers[k])
                sum_tri.append(sum(tri))
                tri.pop()
            tri.pop()
    print(f'#{test_case} {sorted(list(set(sum_tri)))[-5]}')