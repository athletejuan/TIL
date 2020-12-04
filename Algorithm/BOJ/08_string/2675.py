T = int(input())

for _ in range(T):
    R,S = input().split()
    QR = ''
    for c in S:
        QR += c*int(R)
    print(QR)