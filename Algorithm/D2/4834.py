T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = [0] * 10
    nums = list(map(int, list(input())))
    for num in nums:
        cards[num] += 1
    many = 0
    for idx, card in enumerate(cards):
        if card >= many:
            many = card
            card_num = idx
    print('#{} {} {}'.format(tc, card_num, many))


# 1st try
# for test_case in range(1, T+1):
#     num = int(input())
#     nums = input()
#     card = {}
#     count = []
#     for i in set(nums):
#         count.append(nums.count(i))
#         card[i] = nums.count(i)
#     keys = []
#     values = []
#     for key, value in card.items():
#         if value == sorted(count)[-1]:
#             keys.append(int(key))
#             values.append(int(value))
#     print(f'#{test_case} {sorted(keys)[-1]} {sorted(values)[-1]}')