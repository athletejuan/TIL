T = int(input())

for tc in range(1, T+1):
    N,K = map(int, input().split())
    order = []
    nums = list(input())
    for i in range(N//4):
        for j in range(4):
            order.append(int(''.join(nums[j*(N//4):j*(N//4)+(N//4)]), 16))
        nums = [nums[-1]] + nums[:-1]
    print('#{} {}'.format(tc, sorted(list(set(order)), reverse=True)[K-1]))