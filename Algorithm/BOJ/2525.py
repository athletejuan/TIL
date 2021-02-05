A,B = map(int, input().split())
cook = int(input())

if B + (cook % 60) >= 60:
    A += 1
print(str((A + (cook // 60)) % 24) + ' ' + str((B + cook % 60) % 60))