def DFS(used, r, c, cnt):
    global longest
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < R and 0 <= nc < C and not used[ord(alphabet[nr][nc])-65]:
            used[ord(alphabet[nr][nc])-65] = 1
            DFS(used, nr, nc, cnt+1)
            used[ord(alphabet[nr][nc])-65] = 0
    if cnt > longest:
        longest = cnt


R,C = map(int, input().split())
alphabet = [input() for _ in range(R)]
dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
used = [0] * 26
used[ord(alphabet[0][0])-65] = 1
longest = 1
DFS(used, 0, 0, 1)
print(longest)