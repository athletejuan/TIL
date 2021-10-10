N = int(input())

tree = [[] for _ in range(N+1)]
check = [[] for _ in range(N+1)]
q = [1]
result = {}

for _ in range(N-1):
    a,b = list(map(int,input().split()))
    tree[a].append(b)
    tree[b].append(a)

while q:
    parent = q.pop(0)
    for i in tree[parent]:
        if not check[i]:
            result[i] = parent
            q.append(i)
            check[i].append(1)
    
for i in range(2,N+1):
    print(result[i])