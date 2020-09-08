N = int(input())

nodes = list(map(int,input().split()))
tree = [[] for _ in range(N)]
D = int(input())

for idx, node in enumerate(nodes):
    if node < 0:
        root = idx
    else:
        tree[node].append(idx)
leaf = 0
for idx, node in enumerate(tree):
    if root == idx:
        leaf += len(tree[idx])
    elif node: 
        if len(node) == 2:
            leaf += 1
def remove(D):
    global leaf
    if not tree[D]:
        for i in tree:
            if D in i and len(i) > 1:
                leaf -= 1
    else:
        if len(tree[D]) == 1:
            D = int(tree[D][0])
            remove(D)
        else:
            L = D
            D = int(tree[D][0])
            remove(D)
            D = int(tree[L][1])
            remove(D)
if D == root:
    print(0)
else:
    remove(D)
    print(leaf)