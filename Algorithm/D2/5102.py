T = int(input())

def BFS():
    global fin
    candidate = []
    for node in nodes:
        if links[node][G]:
            fin = 1
            return
        else:
            for j in range(1, V+1):
                if links[node][j]:
                    links[node][j] = 0
                    candidate.append(j)
    return candidate

for tc in range(1, T+1):
    V,E = map(int, input().split())
    links = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        x,y = list(map(int, input().split()))
        links[x][y] = links[y][x] = 1
    S,G = map(int, input().split())

    nodes = [S]
    dis, fin = 0, 0
    while nodes:
        nodes = BFS()
        dis += 1
        if fin:
            break
    else:
        dis = 0
    print('#{} {}'.format(tc, dis))


# live code
# def BFS(S):
#     Q = [[S, 0]]
#     visited = [False] * (V+1)
#     visited[S] = True

#     while Q:
#         v, dist = Q.pop(0)

#         if v == G:
#             return dist

#         for i in range(1, V+1):
#             if adj_arr[v][i] and not visited[i]:
#                 Q.append([i, dist+1])
#                 visited[i] = True
#     return 0

# for tc in range(1, T+1):
#     V,E = map(int, input().split())
#     adj_arr = [[0] * (V+1) for _ in range(V+1)]
#     for _ in range(E):
#         x,y = list(map(int, input().split()))
#         adj_arr[x][y] = adj_arr[y][x] = 1
#     S,G = map(int, input().split())

#     print('#{} {}'.format(tc, BFS(S)))