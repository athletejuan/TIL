T = int(input())
ratio = ['211', '221', '122', '411', '132', '231', '114', '312', '213', '112']


def check(code):
    global total
    temp = ok = 0
    for i in range(8):
        if i%2:
            temp += int(code[i])
        else:
            temp += int(code[i])*3
        ok += int(code[i])
    if not temp%10: total += ok


for tc in range(1, T+1):
    N,M = map(int, input().split())
    codes, checked, total = [], [], 0
    for _ in range(N):
        code = input()
        binary = ''
        for i in range(M):
            if ord(code[i]) < 58:
                binary += bin(ord(code[i]) - 48)[2:].zfill(4)
            else:
                binary += bin(ord(code[i]) - 55)[2:]
        codes.append(binary)

    for l in range(N):
        start = False
        first = second = third = gcd = 0
        password = ''
        for m in range(4*M-1, -1, -1):
            if codes[l][m] == '1':
                if not second:
                    start = True
                    third += 1
                else:
                    start = False
                    first += 1
            else:
                if start:
                    second += 1
                else:
                    if first:
                        gcd = min(first, second, third)
                        first //= gcd
                        second //= gcd
                        third //= gcd
                        num = str(first) + str(second) + str(third)
                        for i in range(10):
                            if ratio[i] == num:
                                password = str(i) + password
                            if len(password) > 7:
                                if password not in checked:
                                    checked.append(password)
                                    check(password)
                                password = ''
                        first = second = third = 0

    print('#{} {}'.format(tc, total))