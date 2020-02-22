T = int(input())

for test_case in range(1, T+1):
    stu = list(map(int, input().split()))
    sub = list(map(int, input().split()))
    notyet = []
    for i in range(1,stu[0]+1):
        if i not in sub:
            notyet.append(str(i))
    print(f'#{test_case} {" ".join(notyet)}')