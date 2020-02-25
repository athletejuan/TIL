T = int(input())

for test_case in range(1, T+1):
    num = int(input())
    arr = ['-']+sorted(list(map(int, input().split())))
    new = []
    s = -1
    for i in range(10):
        new.append(arr[s])
        if s>0:
            s -= i+2
        else:
            s += i+2
    print(f'#{test_case} {" ".join(list(map(str, new)))}')