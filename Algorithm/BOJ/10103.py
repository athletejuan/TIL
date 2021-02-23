n = int(input())
CY, SD = 100, 100

for _ in range(n):
    C,S = map(int, input().split())
    if C < S:
        CY -= S
    elif C > S:
        SD -= C
print(CY)
print(SD)