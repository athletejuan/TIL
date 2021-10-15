import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

def GCD(x,y):
    if not y:
        return x
    return GCD(y,x%y)

result = GCD(nums[0], GCD(nums[1], nums[-1]))

for i in range(result//2):
    if not result%(i+1):
        print(i+1)
print(result)