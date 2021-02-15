T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    for i in range(10):
        minmax = i
        for j in range(i+1, N):
            if i%2:
                if nums[minmax] > nums[j]:
                    minmax = j
            else:
                if nums[minmax] < nums[j]:
                    minmax = j
        nums[i],nums[minmax] = nums[minmax],nums[i]
    print(f'#{tc} {" ".join(map(str, nums[:10]))}')


# for test_case in range(1, T+1):
#     num = int(input())
#     arr = ['-']+sorted(list(map(int, input().split())))
#     new = []
#     s = -1
#     for i in range(10):
#         new.append(arr[s])
#         if s>0:
#             s -= i+2
#         else:
#             s += i+2
#     print(f'#{test_case} {" ".join(list(map(str, new)))}')