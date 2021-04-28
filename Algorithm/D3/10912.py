T = int(input())

for test_case in range(1, T+1):
    origin = input()
    single = set()
    for o in origin:
        if origin.count(o)%2:
            single.add(o)
    if not single:
        print(f'#{test_case} Good')
    else:
        print(f'#{test_case} {"".join(sorted(list(single)))}')