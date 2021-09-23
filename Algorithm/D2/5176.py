def inorder(n):
    if n:
        inorder(L[n])
        tree.append(n)
        inorder(R[n])

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    L = [0] * (N+1)
    R = [0] * (N+1)

    for i in range(2, N+1):
        if L[i//2]:
            R[i//2] = i
        else:
            L[i//2] = i
    tree = []
    inorder(1)
    for idx, num in enumerate(tree, start=1):
        if num == 1:
            root = idx
        if num == N//2:
            half = idx
    print('#{} {} {}'.format(tc, root, half))


# live
# T = int(input())
#
# def in_order(v):
#     global num
#     if v <= N:
#         in_order(v*2)
#         tree[v] = num
#         num += 1
#         in_order(v*2+1)
#
# for tc in range(1, T+1):
#     N = int(input())
#     num = 1
#
#     tree = [0] * (N+1)
#     in_order(1)
#     print('#{} {} {}'.format(tc, tree[1], tree[N//2]))
    

# T = int(input())

# class Node:
#     def __init__(self, N):
#         self.li = [0] * (N+1)
#         self.cnt = 1
#         self.numbering(1)

#     def numbering(self, num):
#         if num <= N:
#             self.numbering(num*2)
#             self.li[num] = self.cnt
#             self.cnt += 1
#             self.numbering(num*2+1)
    
#     def result(self):
#         return ' '.join(map(str, (self.li[1], self.li[N//2])))

# for tc in range(1, T+1):
#     N = int(input())
#     node = Node(N)
#     print('#{} {}'.format(tc, node.result()))


# 1st_try
# T = int(input())
#
# def inorder(n):
#     if n:
#         inorder(left[n])
#         tree.append(n)
#         inorder(right[n])
#
# for tc in range(1, T+1):
#     N = int(input())
#     left = [0] * (N+1)
#     right = [0] * (N+1)
#     tree = []
#
#     for i in range(1, N//2+1):
#         left[i] = i*2
#         if i*2+1 < N+1:
#             right[i] = i*2+1
#
#     inorder(1)
#     print('#{}'.format(tc), end=' ')
#     for idx, value in enumerate(tree):
#         if value == 1:
#             print(idx+1, end=' ')
#     for idx, value in enumerate(tree):
#         if value == N//2:
#             print(idx+1)