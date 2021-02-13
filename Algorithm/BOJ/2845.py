L,P = map(int, input().split())
N = map(int, input().split())

for n in N:
    print(n - L*P, end = ' ')
print()