A,B = input().split()
ld = len(B) - len(A) + 1
ds = []
for i in range(ld):
    d = 0
    for j in range(len(A)):
        if A[j] != B[i:i+len(A)][j]:
            d += 1
    ds.append(d)
    if not d:
        break
print(min(ds))