T = int(input())

def BFS():
    global cnt
    while True:
        temp = []
        for i in range(len(dp[cnt])):
            N = dp[cnt][i]
            if N == M:
                print('#{} {}'.format(tc, cnt))
                return
            if N+1 <= 1000000 and not visited[N+1]:
                temp.append(N+1)
                visited[N+1] = 1
            if N-1 > 0 and not visited[N-1]:
                temp.append(N-1)
                visited[N-1] = 1
            if N*2 <= 1000000 and not visited[2*N]:
                temp.append(2*N)
                visited[2*N] = 1
            if N-10 > 0 and not visited[N-10]:
                temp.append(N-10)
                visited[N-10] = 1
        cnt += 1
        dp.append(temp)

for tc in range(1, T+1):
    N,M = map(int, input().split())
    dp = [[N]]
    visited = [0] * 1000001
    visited[N] = 1
    cnt = 0
    BFS()