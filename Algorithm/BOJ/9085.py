import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = input()
    print(sum(map(int, input().split())))