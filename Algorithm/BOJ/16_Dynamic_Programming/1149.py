N = int(input())
rgb = list(map(int, input().split()))

for _ in range(N-1):
    now = list(map(int, input().split()))
    arr = []
    for i in range(3):
        small = 0
        for j in range(3):
            if i != j:
                temp = rgb[j] + now[i]
                if not small or temp < small:
                    small = temp
        arr.append(small)
    rgb = arr
print(min(rgb))