T = int(input())

def dfs(s):
    if s == G:
        return True
    for i in range(1, V+1):
        if adj[s][i]:
            if dfs(i):
                return True
            # if i == G:
            #     return True
            # if dfs(i):
            #     return True

for tc in range(1, T+1):
    V, E = map(int, input().split())
    M = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    adj = [[0]*(V+1) for _ in range(V+1)]
    for a,b in M:
        adj[a][b] = 1

    result = 1 if dfs(S) else 0
    print('#{} {}'.format(tc, result))

    # 반복문
    # stack = [S]
    # visited = [0] * (V+1)
    # while stack:
    #     # flag = False
    #     start = stack.pop()
    #     for i in range(1, V+1):
    #         if adj[start][i]:
    #             # if i == G:
    #             #     print('#{} 1'.format(tc))
    #             #     flag = True
    #             #     break
    #             visited[i] = 1
    #             stack.append(i)
    #     # if flag:
    #     #     break
    # # else:
    # #     print('#{} 0'.format(tc))
    # result = 1 if visited[G] else 0
    # print('#{} {}'.format(tc, result))