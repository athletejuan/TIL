for test_case in range(1,11):
    N = int(input())
    tree = dict()
    root = '1'
    answer = []
    
    class node:
        def __init__(self):
            self.data = None
            self.left = None
            self.right = None
    
    def inorder(node):
        global answer
        if node.left is not None:
            inorder(tree[node.left])
        answer.append(node.data)
        if node.right is not None:
            inorder(tree[node.right])

    points = []
    for i in range(N):
        points.append(input().split())
    for j in range(N):
        if points[j][0] == root:
            tree[root] = node()
            tree[root].data = points[j][1]
            if len(points[j]) > 2:
                tree[root].left = points[j][2]
                tree[points[j][2]] = node()
                tree[points[j][2]].data = points[int(points[j][2])-1][1]
            if len(points[j]) > 3:
                tree[root].right = points[j][3]
                tree[points[j][3]] = node()
                tree[points[j][3]].data = points[int(points[j][3])-1][1]
        else:
            if len(points[j]) > 2:
                tree[points[j][0]].left = points[j][2]
                tree[points[j][2]] = node()
                tree[points[j][2]].data = points[int(points[j][2])-1][1]
            if len(points[j]) > 3:
                tree[points[j][0]].right = points[j][3]
                tree[points[j][3]] = node()
                tree[points[j][3]].data = points[int(points[j][3])-1][1]

    inorder(tree[root])
    print(f"#{test_case} {''.join(answer)}")