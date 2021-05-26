N = int(input())
arr = range(1, N+1)

sel = [0]*N
check = [0]*N

def perm(idx):
    if idx == N:
        print(' '.join(sel))
    else:
        for i in range(N):
            if not check[i]:
                sel[idx] = str(arr[i])
                check[i] = 1
                perm(idx+1)
                check[i] = 0

perm(0)