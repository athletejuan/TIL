N,M = map(int, input().split())
nums = []

def perm(idx, cnt):
    if cnt == M:
        print(*nums)
    else:
        visited = [0]*N
        for j in range(idx):
            visited[j] = 1
        for i in range(N):
            if not visited[i]:
                nums.append(i+1)
                visited[i] = 1
                perm(i, cnt+1)
                nums.pop()
        visited[idx] = 1
perm(0, 0)