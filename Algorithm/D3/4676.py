T = int(input())

for test_case in range(1, T+1):
    text = input()
    num = input()
    pos = sorted(list(map(int, input().split())), reverse=True)
    for i in pos:
        text = text[:i]+'-'+text[i:]
    print(f'#{test_case} {text}')