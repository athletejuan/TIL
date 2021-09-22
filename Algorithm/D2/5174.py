T = int(input())

def inorder(node):
    global cnt
    if node:
        inorder(left[node])
        cnt += 1
        inorder(right[node])

for tc in range(1, T+1):
    E,N = map(int, input().split())
    nodes = list(map(int, input().split()))
    cnt = 0

    left = [0] * (E+2)
    right = [0] * (E+2)

    for i in range(E):
        if left[nodes[i*2]]:
            right[nodes[i*2]] = nodes[i*2+1]
        else:
            left[nodes[i*2]] = nodes[i*2+1]
    inorder(N)
    print('#{} {}'.format(tc, cnt))


# 2nd_try
T = int(input())

def sub_tree(node):
    global cnt
    if node[0]:
        sub_tree(tree[node[0]])
    if node[1]:
        sub_tree(tree[node[1]])
    cnt += 1

for tc in range(1, T+1):
    E,N = map(int, input().split())
    vertex = list(map(int, input().split()))
    tree = [[0,0] for _ in range(E+2)]
    cnt = 0

    for i in range(E):
        if tree[vertex[2*i]][0]:
            tree[vertex[2*i]][1] = vertex[2*i+1]
        else:
            tree[vertex[2*i]][0] = vertex[2*i+1]

    sub_tree(tree[N])
    print('#{} {}'.format(tc, cnt))


# 1st_try
T = int(input())

def subtree(N):
    global cnt
    cnt += 1
    for j in tree[N]:
        subtree(j)

for tc in range(1, T+1):
    E,N = map(int, input().split())
    vertex = list(map(int, input().split()))
    cnt = 0
    tree = [[] for _ in range(E+2)]
    for i in range(0, E*2, 2):
        a = vertex[i]
        b = vertex[i+1]
        tree[a].append(b)
    subtree(N)
    print('#{} {}'.format(tc, cnt))