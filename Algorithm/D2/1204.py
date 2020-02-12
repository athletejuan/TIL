T = int(input())

for t in range(1, T+1):
    test_case = input()
    numbers = list(map(int, input().split()))
    nums = list(set(numbers))
    count_list = []
    for i in nums:
        count_list.append(numbers.count(i))
    count_dict = dict(zip(nums, count_list))
    for key, value in count_dict.items():
        if value == max(count_dict.values()):
            print(f'#{test_case} {key}')