T = int(input())

for test_case in range(1, T+1):
    num = int(input())
    nums = input()
    card = {}
    count = []
    for i in set(nums):
        count.append(nums.count(i))
        card[i] = nums.count(i)
    keys = []
    values = []
    for key, value in card.items():
        if value == sorted(count)[-1]:
            keys.append(int(key))
            values.append(int(value))
    print(f'#{test_case} {sorted(keys)[-1]} {sorted(values)[-1]}')