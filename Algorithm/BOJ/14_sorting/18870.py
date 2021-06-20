N = int(input())
nums = list(map(int, input().split()))
order = sorted(set(nums))

axis = {order[i]: i for i in range(len(order))}
for num in nums:
    print(axis[num], end=' ')