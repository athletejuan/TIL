S = input()
arr = []

for i in range(len(S)):
    arr.append(S[i:])
for j in sorted(arr):
    print(j)