def dfs(s):
    global result
    if s == 99:
        result = 1
        return
    for i in range(len(links[s])):
        dfs(links[s][i])

for tc in range(1, 11):
    tc,E = map(int, input().split())
    edges = list(map(int, input().split()))
    links = [[] for _ in range(101)]
    result = 0
    for i in range(E):
        links[edges[i*2]].append(edges[i*2+1])

    for j in range(len(links[0])):
        dfs(links[0][j])

    print('#{} {}'.format(tc, result))


# lecture code
# def check_path(G):
#     # 방문 정점
#     visited = [0 for _ in range(100)]
#     # 가장 첫번째 정점 넣어 놓고 시작
#     stack = [0]

#     # stack이 빌 때까지 (모든 정점 방문)
#     while stack:
#         # 특정 정점을 stack에서 꺼내서
#         v = stack.pop()
#         # 그 정점에 방문하지 않았다면
#         if not visited[v]:
#             # 방문처리하고
#             visited[v] = 1
#             # 인접 정점 찾아서 stack에 추가
#             stack += G[v]

#     # 최종적으로 99정점의 방문여부 return
#     return visited[99]

# T = 1
# for _ in range(1, T+1):
#     tc, E = input().split()
#     G = [[] for _ in range(100)]
#     V = list(map(int, input().split()))
#     for idx in range(0, len(V), 2):
#         # fr -> 정점
#         fr = V[idx]
#         # to -> 해당 정점에 연결된 값
#         to = V[idx+1]
#         # 인접 리스트 생성
#         G[fr].append(to)
#     print(G)
#     result = check_path(G)
#     print('#{} {}'.format(tc, result))