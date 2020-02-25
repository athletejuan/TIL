T = int(input())

for test_case in range(1, T+1):
    card = input()
    count = len(card)//3
    cl = []
    sn = dn = hn = cn = 13
    for i in range(count):
        i *= 3
        cl.append(card[i:i+3])
    if len(cl) == len(set(cl)):
        for i in cl:
            if i[0] == 'S':
                sn -= 1
            elif i[0] == 'D':
                dn -= 1
            elif i[0] == 'H':
                hn -= 1
            elif i[0] == 'C':
                cn -= 1
        print(f'#{test_case} {sn} {dn} {hn} {cn}')
    else:
        print(f'#{test_case} ERROR')