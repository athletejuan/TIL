N,K = map(int, input().split())

circle = []
for i in range(1, N+1):
    circle.append(i)

li = []
josep = 0
while circle:
    josep += (K-1)
    while josep >= len(circle):
        josep -= len(circle)
    li.append(str(circle.pop(josep)))
print(f'<{", ".join(li)}>')