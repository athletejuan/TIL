while True:
    try:
        n = int(input())
        num, cnt = 1, 1
    except EOFError:
        break
    while num%n:
        num = num * 10 + 1
        cnt += 1
    print(cnt)