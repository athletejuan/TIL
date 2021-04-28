T = int(input())

for tc in range(1, T+1):
    D,L,N = map(int, input().split())
    total = D * N
    for i in range(N):
        plus = D * L * i // 100
        total += plus
    print(f'#{tc} {total}')