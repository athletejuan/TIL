T = int(input())

for _ in range(T):
    idx, text = input().split()
    print(text[:int(idx)-1]+text[int(idx):])