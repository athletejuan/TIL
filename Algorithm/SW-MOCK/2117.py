T = int(input())
 
 
def security(r,c,k):
    global max_home
    while k:
        width, homes = 1, 0
        cost = k**2 + (k-1)**2
        for i in range(2*k, 0, -1):
            if i > k:
                for j in range(width):
                    if 0 <= r-i+k < N and 0 <= c+j-(width//2) < N:
                        homes += city[r-i+k][c+j-(width//2)]
                width += 2
            else:
                width -= 2
                for j in range(width-2):
                    if 0 <= r-i+k < N and 0 <= c+j-(width//2)+1 < N:
                        homes += city[r-i+k][c+j-(width//2)+1]
        if cost <= homes*M and max_home < homes:
            max_home = homes
            return
        k -= 1
 
 
for tc in range(1, T+1):
    N,M = map(int, input().split())
    K = N if N%2 else N+1
    city = [list(map(int, input().split())) for _ in range(N)]
    max_home = 0
    for i in range(N):
        for j in range(N):
            security(i,j,K)
    print(f'#{tc} {max_home}')