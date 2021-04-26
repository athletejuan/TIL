T = int(input())
number = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

def cryptogram(row):
    global total
    for i in range(M-1, -1, -1):
        if row[i] == '1':
            pw = row[i-55:i+1]
            pwcode = []
            for j in range(8):
                for k in range(len(number)):
                    if number[k] == pw[j*7:(j*7+7)]:
                        pwcode.append(k)
            odd = even = 0
            for s in range(8):
                if s%2:
                    even += pwcode[s]
                else:
                    odd += pwcode[s]
                total += pwcode[s]
            return False if (odd*3 + even)%10 else True

for tc in range(1, T+1):
    N,M = map(int, input().split())
    code = [input() for i in range(N)]
    total = 0
    for row in code:
        if cryptogram(row):
            print('#{} {}'.format(tc, total))
            break
    else:
        print('#{} 0'.format(tc))