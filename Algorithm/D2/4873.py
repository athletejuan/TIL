T = int(input())

for test_case in range(1, T+1):
    text = input()
    tl = []
    for i in text:
        if not tl or tl[-1] != i:
            tl.append(i)
        else:
            tl.pop()
    print(f'#{test_case} {len(tl)}')