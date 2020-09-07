T = int(input())

for t in range(T):
    message = input()
    first = []
    last = []
    for idx, char in enumerate(message):
        if idx%2:
            last.append(char)
        else:
            first.append(char)
    print(''.join(first)+''.join(last))