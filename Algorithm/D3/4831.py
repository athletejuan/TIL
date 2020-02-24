T = int(input())

for test_case in range(1, T+1):
    nums = list(map(int, input().split()))
    stop = list(map(int, input().split()))
    start = 0
    count = 0
    while (start + nums[0]) < nums[1]:
        for i in range(nums[0], 0, -1):
            if start + i in stop:
                start += i
                count += 1
                break
            elif (start + nums[0]) > nums[1]:
                print(f'#{test_case} {count}')
        else:
            print(f'#{test_case} 0')
            break
    else:
        print(f'#{test_case} {count}')