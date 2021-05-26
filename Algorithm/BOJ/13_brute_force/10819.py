N = int(input())
arr = list(map(int, input().split()))

sel = [0] * N
check = [0] * N
max_val = 0

def perm(idx):
    global max_val
    if idx == N:
        total = 0
        for i in range(N-1):
            total += abs(sel[i] - sel[i+1])
        if not max_val or total > max_val:
            max_val = total
    else:
        for i in range(N):
            if not check[i]:
                sel[idx] = arr[i]
                check[i] = 1
                perm(idx+1)
                check[i] = 0

perm(0)
print(max_val)