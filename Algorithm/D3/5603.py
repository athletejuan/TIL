T = int(input())

for tc in range(1, T+1):
    N = int(input())
    hay = []
    c = 0
    for _ in range(N):
        hay.append(int(input()))
    avg = sum(hay)//N
    for i in hay:
        if i < avg:
            c += avg-i
    print(f'#{tc} {c}')