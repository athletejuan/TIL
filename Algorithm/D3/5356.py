T = int(input())

for tc in range(1, T+1):
    l = 0
    arr = []
    col = []
    for _ in range(5):
        row = list(input())
        if len(row) > l:
            l = len(row)
        arr.append(row)
    for i in range(l):
        for j in range(5):
            if arr[j]:
                col.append(arr[j].pop(0))
    print(f'#{tc} {"".join(col)}')