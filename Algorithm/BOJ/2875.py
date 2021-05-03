N,M,K = map(int, input().split())

team = M
if N < 2*M:
    team = N//2
if N+M - (3*team) - K < 0:
    team -= (K+2 - (N+M - (3*team)))//3
print(team)