def DFS(r,c,num,l):
    if l == 6:
        nums.add(num)
        return
    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < 5 and 0 <= nc < 5:
            DFS(nr, nc, num+board[nr][nc], l+1)


board = [list(input().split()) for _ in range(5)]
dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
nums = set()
for i in range(5):
    for j in range(5):
        DFS(i,j,board[i][j],1)
print(len(nums))