def inorder(node):
    if node:
        inorder(left[node])
        print(tree[node], end='')
        inorder(right[node])

for tc in range(1, 11):
    N = int(input())
    tree = [0]*(N+1)
    left = [0]*(N+1)
    right = [0]*(N+1)

    for i in range(N):
        node = input().split()
        if len(node) > 2:
            left[int(node[0])] = int(node[2])
            if len(node) > 3:
                right[int(node[0])] = int(node[3])
        tree[int(node[0])] = node[1]

    print('#{}'.format(tc), end=' ')
    inorder(1)
    print()


# 1st try
# for test_case in range(1,11):
#     N = int(input())
#     tree = dict()
#     root = '1'
#     answer = []
#
#     class node:
#         def __init__(self):
#             self.data = None
#             self.left = None
#             self.right = None
#
#     def inorder(node):
#         global answer
#         if node.left is not None:
#             inorder(tree[node.left])
#         answer.append(node.data)
#         if node.right is not None:
#             inorder(tree[node.right])
#
#     points = []
#     for i in range(N):
#         points.append(input().split())
#     for j in range(N):
#         if points[j][0] == root:
#             tree[root] = node()
#             tree[root].data = points[j][1]
#             if len(points[j]) > 2:
#                 tree[root].left = points[j][2]
#                 tree[points[j][2]] = node()
#                 tree[points[j][2]].data = points[int(points[j][2])-1][1]
#             if len(points[j]) > 3:
#                 tree[root].right = points[j][3]
#                 tree[points[j][3]] = node()
#                 tree[points[j][3]].data = points[int(points[j][3])-1][1]
#         else:
#             if len(points[j]) > 2:
#                 tree[points[j][0]].left = points[j][2]
#                 tree[points[j][2]] = node()
#                 tree[points[j][2]].data = points[int(points[j][2])-1][1]
#             if len(points[j]) > 3:
#                 tree[points[j][0]].right = points[j][3]
#                 tree[points[j][3]] = node()
#                 tree[points[j][3]].data = points[int(points[j][3])-1][1]
#
#     inorder(tree[root])
#     print(f"#{test_case} {''.join(answer)}")