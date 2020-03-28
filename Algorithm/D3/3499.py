T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    cards = input().split()
    new = []
    if N%2:
        front = cards[:(N//2)+1]
        back = cards[(N//2)+1:]
    else:
        front = cards[:(N//2)]
        back = cards[(N//2):]
    while back:
        new.append(front.pop(0))
        new.append(back.pop(0))
    if front:
        new.append(front.pop())
    print(f'#{test_case} {" ".join(new)}')