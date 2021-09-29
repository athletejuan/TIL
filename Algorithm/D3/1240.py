T = int(input())
number = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']


def password():
    for row in code:
        for i in range(M-1, -1, -1):
            if row[i] == '1':
                pw = row[i-55:i+1]
                temp = valid = 0
                for j in range(8):
                    for k in range(10):
                        if number[k] == pw[j*7:(j+1)*7]:
                            if j%2:
                                temp += k
                            else:
                                temp += k*3
                            valid += k
                return 0 if temp%10 else valid


for tc in range(1, T+1):
    N,M = map(int, input().split())
    code = [input() for i in range(N)]
    print('#{} {}'.format(tc, password()))