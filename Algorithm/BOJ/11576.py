A,B = map(int, input().split())
m = int(input())
nums = list(map(int, input().split()))
decimal = 0
result = []

for i in range(m):
    decimal += nums[i]*(A**(m-i-1))

while decimal:
    result.append(str(decimal % B))
    decimal //= B

result.reverse()
print(' '.join(result))