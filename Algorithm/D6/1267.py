def BFS(nodes):
    global flow
    while nodes:
        cand, after = [], []
        for node in nodes:
            for i in range(1, V+1):
                if links[node][i]:
                    cand.append(i)
                    links[node][i] = 0
        for c in cand:
            for i in range(1, V+1):
                if links[i][c]:
                    break
            else:
                if c not in flow:
                    flow.append(c)
                after.append(c)
        return BFS(after)

for tc in range(1, 11):
    V,E = map(int, input().split())
    nodes = list(map(int, input().split()))
    links = [[0]*(V+1) for _ in range(V+1)]
    for i in range(0, 2*E, 2):
        links[nodes[i]][nodes[i+1]] = 1
    flow = []

    for j in range(1, V+1):
        for k in range(1, V+1):
            if links[k][j]:
                break
        else:
            flow.append(j)
    BFS(flow)
    print('#{} {}'.format(tc, ' '.join(map(str, flow))))