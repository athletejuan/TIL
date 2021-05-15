import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    univs = [input().split() for i in range(N)]
    print(sorted(univs, key=lambda x: int(x[1]))[-1][0])
    # univs.sort(key=lambda x: int(x[1]))
    # print(univs[-1][0])