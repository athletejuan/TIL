T = int(input())

for test_case in range(1, T+1):
    nums = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    ps_li = []
    for i in range(nums[0]-nums[1]+1):
        ps = 0
        for j in range(i, nums[1]+i):
            ps += arr[j]
        ps_li.append(ps)
    print(f'#{test_case} {sorted(ps_li)[-1] - sorted(ps_li)[0]}')