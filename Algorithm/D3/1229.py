for tc in range(1, 11):
    N = int(input())
    origin = list(input().split())
    C = int(input())
    command = list(input().split())
    for i in range(len(command)):
        if command[i] == 'I':
            idx = int(command[i+1])
            length = int(command[i+2])
            origin = origin[:idx] + command[i+3:i+3+length] + origin[idx:]
        elif command[i] == 'D':
            idx = int(command[i+1])
            length = int(command[i+2])
            origin = origin[:idx] + origin[(idx+length):]
    print('#{} {}'.format(tc, ' '.join(origin[:10])))