def BFS(s):
    contact, big, temp = [s], s, []
    while contact:
        start = contact.pop()
        if start > big:
            big = start
        for j in adj[start]:
            if not visited[j]:
                temp.append(j)
                visited[j] = 1
        if not contact:
            contact, temp = temp, []
            if contact:
                big = 0
    return big
 
 
for tc in range(1, 11):
    N,S = map(int, input().split())
    fromto = list(map(int, input().split()))
    adj = [[] for _ in range(101)]
    visited = [0] * 101
 
    for i in range(N//2):
        adj[fromto[i*2]].append(fromto[i*2+1])
    print(f'#{tc} {BFS(S)}')