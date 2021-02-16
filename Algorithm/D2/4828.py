T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    for i in range(N-1):
        for j in range(N-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    print(f'#{tc} {nums[-1] - nums[0]}')


# 1st try
# for test_case in range(1, T+1):
#     num = input()
#     nums = list(map(int, input().split()))
#     sn = sorted(nums)
#     print(f'#{test_case} {sn[-1] - sn[0]}')