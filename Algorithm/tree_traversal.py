N = int(input())
tree = [[] for _ in range(N+1)]
nodes = list(map(int, input().split()))

def preorder(node):
    print(node, end=' ')
    for i in range(len(tree[node])):
        preorder(tree[node][i])

def inorder(node):
    if tree[node]:
        inorder(tree[node][0])
        if len(tree[node]) > 1:
            print(node, end=' ')
            inorder(tree[node][1])
            return
    print(node, end=' ')

def postorder(node):
    if tree[node]:
        for i in range(len(tree[node])):
            postorder(tree[node][i])
    print(node, end= ' ')

for i in range(N-1):
    tree[nodes[i*2]].append(nodes[i*2+1])

preorder(1)
print()
inorder(1)
print()
postorder(1)
print()