N = int(input())
A = list(map(int, input().split()))
S = sorted(A)

for i in range(len(A)):
    for idx, item in enumerate(A):
        if S[i] == item:
            A[idx] = str(i)
            break
print(' '.join(A))