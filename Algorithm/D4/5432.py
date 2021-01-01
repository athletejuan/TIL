T = int(input())

for tc in range(1, T+1):
    st = input()
    stick = 0
    piece = 0
    for i in range(len(st)):
        if st[i] == '(':
            stick += 1
        else:
            stick -= 1
            if st[i-1] == ')':
                piece += 1
            else:
                piece += stick
    print(f'#{tc} {piece}')