A = int(input())
B = int(input())
ans = A*B
for _ in range(3):
    print(A*(B%10))
    B = B//10
print(ans)