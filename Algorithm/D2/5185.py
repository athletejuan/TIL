T = int(input())

def binary(n):
    bi = ''
    for i in range(4):
        bi = str(n%2) + bi
        n //= 2
    return bi

for tc in range(1, T+1):
    N,hexa = input().split()
    bi_num = ''
    for i in range(int(N)):
        bi_num += binary(ord(hexa[i]) - 55 if ord(hexa[i]) > 64 else ord(hexa[i]) - 48)
    print('#{} {}'.format(tc, bi_num))