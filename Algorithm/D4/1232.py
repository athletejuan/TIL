def cal(op):
    if len(op) < 2:
        return int(op[0])
    else:
        if op[0] == '+':
            return cal(tree[int(op[1])]) + cal(tree[int(op[2])])
        elif op[0] == '-':
            return cal(tree[int(op[1])]) - cal(tree[int(op[2])])
        elif op[0] == '*':
            return cal(tree[int(op[1])]) * cal(tree[int(op[2])])
        else:
            return cal(tree[int(op[1])]) // cal(tree[int(op[2])])

for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)
    for i in range(N):
        node = input().split()
        tree[int(node[0])] = node[1:]

    print('#{} {}'.format(tc, cal(tree[1])))