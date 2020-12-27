import sys
N = int(sys.stdin.readline())

answer = 0
for _ in range(N):
    answer += int(sys.stdin.readline())
print(answer - (N-1))