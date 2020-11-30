T = int(input())

for test_case in range(1, T+1):
    origin = input()
    mirror = []
    for o in origin:
        if o == 'b':
            mirror.append('d')
        elif o == 'd':
            mirror.append('b')
        elif o == 'p':
            mirror.append('q')
        else:
            mirror.append('p')
    print(f'#{test_case} {"".join(reversed(mirror))}')