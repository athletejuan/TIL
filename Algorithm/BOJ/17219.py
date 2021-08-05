N,M = map(int, input().split())
sites = {}

for _ in range(N):
    info = input().split()
    sites[info[0]] = info[1]

for i in range(M):
    site = input()
    print(sites[site])