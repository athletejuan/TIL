def comb(N, picked, toPick):
    global tri_idx
    if not toPick:
        tri_sum = 0
        for j in picked:
            tri_sum += j
            if tri_sum > 1000:
                return
        if tri_sum < 1001:
            tri_idx[tri_sum] = 1
            return

    mini = 0 if not picked else tri.index(picked[-1])
    for i in range(mini, N):
        picked.append(tri[i])
        comb(N, picked, toPick-1)
        picked.pop()


T = int(input())
tri_idx = [0] * 1001
tri, i = [1], 2
while tri[-1]+i < 1000:
    tri.append(tri[-1]+i)
    i += 1
comb(len(tri), [], 3)

for _ in range(T):
    K = int(input())
    print(tri_idx[K])