N = int(input())

A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)
mini = 0
for _ in range(N):
    mini += (A.pop(0) * B.pop(0))
print(mini)