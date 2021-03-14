N = int(input())

remain = 0
for _ in range(N):
    S,A = map(int, input().split())
    remain += A%S
print(remain)