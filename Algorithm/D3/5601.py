T = int(input())

for tc in range(1, T+1):
    N = input()
    juice = []
    for _ in range(int(N)):
        juice.append('1/'+N)
    print(f'#{tc} {" ".join(juice)}')