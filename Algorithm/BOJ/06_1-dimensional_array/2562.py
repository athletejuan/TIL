max_num = 0
idx = 0
for _ in range(9):
    idx += 1
    num = int(input())
    if max_num < num:
        max_num = num
        max_idx = idx
print(max_num)
print(max_idx)