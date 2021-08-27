def preorder(n):
    if n:
        print(n, end=' ')
        preorder(left[n])
        preorder(right[n])

def inorder(n):
    if n:
        inorder(left[n])
        print(n, end=' ')
        inorder(right[n])

def postorder(n):
    if n:
        postorder(left[n])
        postorder(right[n])
        print(n, end=' ')

V = int(input())        # 정점 수
tree = [[] for _ in range(V+1)]
edges = list(map(int, input().split()))
E = V-1                 # 간선 수
left = [0]*(V+1)
right = [0]*(V+1)

for i in range(E):
    p,c = edges[i*2], edges[i*2+1]
    if not left[p]:
        left[p] = c
    else:
        right[p] = c
        
preorder(1)
print()
inorder(1)
print()
postorder(1)
print()


# 1st try
# N = int(input())
# tree = [[] for _ in range(N+1)]
# nodes = list(map(int, input().split()))

# def preorder(node):
#     print(node, end=' ')
#     for i in range(len(tree[node])):
#         preorder(tree[node][i])

# def inorder(node):
#     if tree[node]:
#         inorder(tree[node][0])
#         if len(tree[node]) > 1:
#             print(node, end=' ')
#             inorder(tree[node][1])
#             return
#     print(node, end=' ')

# def postorder(node):
#     if tree[node]:
#         for i in range(len(tree[node])):
#             postorder(tree[node][i])
#     print(node, end= ' ')

# for i in range(N-1):
#     tree[nodes[i*2]].append(nodes[i*2+1])

# preorder(1)
# print()
# inorder(1)
# print()
# postorder(1)
# print()